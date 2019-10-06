import asyncio
import logging
from typing import List
import uuid

from grpclib.server import Server
from grpclib.client import Channel

from .grpc import (
    api_pb2, api_grpc, constants
)


log = logging.getLogger('ai.backend.accelerator.server')


class PluginException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class DevicePluginServicer(api_grpc.DevicePluginBase):
    devices: List[str]

    def __init__(self):
        self.devices = [str(uuid.uuid4()) for _ in range(len(5))]

    async def GetDevicePluginOptions(self, stream):
        log.info('gRPC::GetDevicePluginOptions')
        return api_pb2.DevicePluginOptions()

    async def ListAndWatch(self, stream):
        log.info('gRPC::ListAndWatch')
        await stream.send_message(api_pb2.ListAndWatchResponse(
            devices=[
                api_pb2.Device(ID=device_id, health='Healthy')
                for device_id in self.devices
            ]
        ))

    async def Allocate(self, stream):
        log.info('gRPC::Allocate')
        response = api_pb2.AllocateResponse()
        request_message: api_pb2.AllocateRequest = await stream.get_message()

        for request in request_message.container_requests:
            log.debug('Allocation requested for devices {0}',
                      request.deviceIDs)
            for deviceId in request.deviceIDs:
                if deviceId not in self.devices:
                    log.error('device ID {0} not valid', deviceId)
                    break
            else:
                device_list_str = ','.join(request.deviceIDs)
                envs = {
                    'NVIDIA_VISIBLE_DEVICES': device_list_str
                }

                response.container_responses.append(
                    api_pb2.ContainerAllocateResponse(envs=envs)
                )
        await stream.send_message(response)

    async def PreStartContainer(self, stream):
        log.info('gRPC::PreStartContainer')
        await stream.send_message(api_pb2.PreStartContainerResponse())


class DevicePluginServer:
    socket_path: str
    device_plugin: DevicePluginServicer
    plugin_server: Server

    def __init__(self):
        self.device_plugin = DevicePluginServicer()

    async def register(self):
        resource_name = 'backend.ai/fake-cuda'
        register_channel = Channel(path=constants.kubelet_socket)

        log.debug('Trying to connect to gRPC Channel {0}',
                  constants.kubelet_socket)
        register_client = api_grpc.RegistrationStub(register_channel)

        log.debug('Created gRPC Client')

        request = api_pb2.RegisterRequest(
            version=constants.version,
            endpoint='backend-ai.sock',
            resource_name=resource_name
        )

        log.debug('Trying to send request {0}', str(request))

        try:
            await register_client.Register(request)
        except Exception as e:
            print(e)
            log.exception(e)
            log.error('Error while registering: ' + str(e))
        log.debug('Device plugin registered. Closing channel')
        register_channel.close()

    async def start(self):
        await self.device_plugin.ainit()
        self.plugin_server = Server([self.device_plugin])

        log.info('Listening to gRPC request from {0}/backend-ai.sock',
                 constants.device_plugin_path)
        try:
            await self.plugin_server.start(
                path=f'{constants.device_plugin_path}/backend-ai.sock'
            )
        except Exception as e:
            log.error('Error while starting plugin server')
            log.exception(e)

        log.info('Registering Device Plugin to Kubelet')
        try:
            await self.register()
        except Exception as e:
            log.error('Error while registering device plugin')
            print(e)
            log.exception(e)

        await self.plugin_server.wait_closed()


def main():
    server = DevicePluginServer()

    try:
        asyncio.get_event_loop().run_until_complete(server.start())
    except Exception as e:
        log.exception(e)
        log.error("Could not contact Kubelet, retrying.")
        log.error("Did you enable the device plugin feature gate?")
        exit(-1)
    finally:
        exit(0)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    main()
