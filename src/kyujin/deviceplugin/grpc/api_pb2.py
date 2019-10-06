# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import gogo_pb2 as gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='v1beta1',
  syntax='proto3',
  serialized_options=_b('\330\341\036\000\200\342\036\001\310\341\036\001\310\342\036\001\340\342\036\001\320\342\036\001\220\343\036\000'),
  serialized_pb=_b('\n\tapi.proto\x12\x07v1beta1\x1a\ngogo.proto\"1\n\x13\x44\x65vicePluginOptions\x12\x1a\n\x12pre_start_required\x18\x01 \x01(\x08\"z\n\x0fRegisterRequest\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x02 \x01(\t\x12\x15\n\rresource_name\x18\x03 \x01(\t\x12-\n\x07options\x18\x04 \x01(\x0b\x32\x1c.v1beta1.DevicePluginOptions\"\x07\n\x05\x45mpty\"8\n\x14ListAndWatchResponse\x12 \n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x0f.v1beta1.Device\"$\n\x06\x44\x65vice\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x0e\n\x06health\x18\x02 \x01(\t\".\n\x18PreStartContainerRequest\x12\x12\n\ndevicesIDs\x18\x01 \x03(\t\"\x1b\n\x19PreStartContainerResponse\"P\n\x0f\x41llocateRequest\x12=\n\x12\x63ontainer_requests\x18\x01 \x03(\x0b\x32!.v1beta1.ContainerAllocateRequest\".\n\x18\x43ontainerAllocateRequest\x12\x12\n\ndevicesIDs\x18\x01 \x03(\t\"S\n\x10\x41llocateResponse\x12?\n\x13\x63ontainer_responses\x18\x01 \x03(\x0b\x32\".v1beta1.ContainerAllocateResponse\"\xc8\x02\n\x19\x43ontainerAllocateResponse\x12:\n\x04\x65nvs\x18\x01 \x03(\x0b\x32,.v1beta1.ContainerAllocateResponse.EnvsEntry\x12\x1e\n\x06mounts\x18\x02 \x03(\x0b\x32\x0e.v1beta1.Mount\x12$\n\x07\x64\x65vices\x18\x03 \x03(\x0b\x32\x13.v1beta1.DeviceSpec\x12H\n\x0b\x61nnotations\x18\x04 \x03(\x0b\x32\x33.v1beta1.ContainerAllocateResponse.AnnotationsEntry\x1a+\n\tEnvsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"E\n\x05Mount\x12\x16\n\x0e\x63ontainer_path\x18\x01 \x01(\t\x12\x11\n\thost_path\x18\x02 \x01(\t\x12\x11\n\tread_only\x18\x03 \x01(\x08\"L\n\nDeviceSpec\x12\x16\n\x0e\x63ontainer_path\x18\x01 \x01(\t\x12\x11\n\thost_path\x18\x02 \x01(\t\x12\x13\n\x0bpermissions\x18\x03 \x01(\t2F\n\x0cRegistration\x12\x36\n\x08Register\x12\x18.v1beta1.RegisterRequest\x1a\x0e.v1beta1.Empty\"\x00\x32\xbc\x02\n\x0c\x44\x65vicePlugin\x12H\n\x16GetDevicePluginOptions\x12\x0e.v1beta1.Empty\x1a\x1c.v1beta1.DevicePluginOptions\"\x00\x12\x41\n\x0cListAndWatch\x12\x0e.v1beta1.Empty\x1a\x1d.v1beta1.ListAndWatchResponse\"\x00\x30\x01\x12\x41\n\x08\x41llocate\x12\x18.v1beta1.AllocateRequest\x1a\x19.v1beta1.AllocateResponse\"\x00\x12\\\n\x11PreStartContainer\x12!.v1beta1.PreStartContainerRequest\x1a\".v1beta1.PreStartContainerResponse\"\x00\x42\x1c\xd8\xe1\x1e\x00\x80\xe2\x1e\x01\xc8\xe1\x1e\x01\xc8\xe2\x1e\x01\xe0\xe2\x1e\x01\xd0\xe2\x1e\x01\x90\xe3\x1e\x00\x62\x06proto3')
  ,
  dependencies=[gogo__pb2.DESCRIPTOR,])




_DEVICEPLUGINOPTIONS = _descriptor.Descriptor(
  name='DevicePluginOptions',
  full_name='v1beta1.DevicePluginOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pre_start_required', full_name='v1beta1.DevicePluginOptions.pre_start_required', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=83,
)


_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='v1beta1.RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='v1beta1.RegisterRequest.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='v1beta1.RegisterRequest.endpoint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='v1beta1.RegisterRequest.resource_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='v1beta1.RegisterRequest.options', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=207,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='v1beta1.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=216,
)


_LISTANDWATCHRESPONSE = _descriptor.Descriptor(
  name='ListAndWatchResponse',
  full_name='v1beta1.ListAndWatchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='devices', full_name='v1beta1.ListAndWatchResponse.devices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=274,
)


_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='v1beta1.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='v1beta1.Device.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='health', full_name='v1beta1.Device.health', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=312,
)


_PRESTARTCONTAINERREQUEST = _descriptor.Descriptor(
  name='PreStartContainerRequest',
  full_name='v1beta1.PreStartContainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='devicesIDs', full_name='v1beta1.PreStartContainerRequest.devicesIDs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=360,
)


_PRESTARTCONTAINERRESPONSE = _descriptor.Descriptor(
  name='PreStartContainerResponse',
  full_name='v1beta1.PreStartContainerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=389,
)


_ALLOCATEREQUEST = _descriptor.Descriptor(
  name='AllocateRequest',
  full_name='v1beta1.AllocateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_requests', full_name='v1beta1.AllocateRequest.container_requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=391,
  serialized_end=471,
)


_CONTAINERALLOCATEREQUEST = _descriptor.Descriptor(
  name='ContainerAllocateRequest',
  full_name='v1beta1.ContainerAllocateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='devicesIDs', full_name='v1beta1.ContainerAllocateRequest.devicesIDs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=519,
)


_ALLOCATERESPONSE = _descriptor.Descriptor(
  name='AllocateResponse',
  full_name='v1beta1.AllocateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_responses', full_name='v1beta1.AllocateResponse.container_responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=521,
  serialized_end=604,
)


_CONTAINERALLOCATERESPONSE_ENVSENTRY = _descriptor.Descriptor(
  name='EnvsEntry',
  full_name='v1beta1.ContainerAllocateResponse.EnvsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1beta1.ContainerAllocateResponse.EnvsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1beta1.ContainerAllocateResponse.EnvsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=840,
  serialized_end=883,
)

_CONTAINERALLOCATERESPONSE_ANNOTATIONSENTRY = _descriptor.Descriptor(
  name='AnnotationsEntry',
  full_name='v1beta1.ContainerAllocateResponse.AnnotationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1beta1.ContainerAllocateResponse.AnnotationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1beta1.ContainerAllocateResponse.AnnotationsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=885,
  serialized_end=935,
)

_CONTAINERALLOCATERESPONSE = _descriptor.Descriptor(
  name='ContainerAllocateResponse',
  full_name='v1beta1.ContainerAllocateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envs', full_name='v1beta1.ContainerAllocateResponse.envs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mounts', full_name='v1beta1.ContainerAllocateResponse.mounts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devices', full_name='v1beta1.ContainerAllocateResponse.devices', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='v1beta1.ContainerAllocateResponse.annotations', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONTAINERALLOCATERESPONSE_ENVSENTRY, _CONTAINERALLOCATERESPONSE_ANNOTATIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=607,
  serialized_end=935,
)


_MOUNT = _descriptor.Descriptor(
  name='Mount',
  full_name='v1beta1.Mount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_path', full_name='v1beta1.Mount.container_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host_path', full_name='v1beta1.Mount.host_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_only', full_name='v1beta1.Mount.read_only', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=937,
  serialized_end=1006,
)


_DEVICESPEC = _descriptor.Descriptor(
  name='DeviceSpec',
  full_name='v1beta1.DeviceSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_path', full_name='v1beta1.DeviceSpec.container_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host_path', full_name='v1beta1.DeviceSpec.host_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='v1beta1.DeviceSpec.permissions', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1008,
  serialized_end=1084,
)

_REGISTERREQUEST.fields_by_name['options'].message_type = _DEVICEPLUGINOPTIONS
_LISTANDWATCHRESPONSE.fields_by_name['devices'].message_type = _DEVICE
_ALLOCATEREQUEST.fields_by_name['container_requests'].message_type = _CONTAINERALLOCATEREQUEST
_ALLOCATERESPONSE.fields_by_name['container_responses'].message_type = _CONTAINERALLOCATERESPONSE
_CONTAINERALLOCATERESPONSE_ENVSENTRY.containing_type = _CONTAINERALLOCATERESPONSE
_CONTAINERALLOCATERESPONSE_ANNOTATIONSENTRY.containing_type = _CONTAINERALLOCATERESPONSE
_CONTAINERALLOCATERESPONSE.fields_by_name['envs'].message_type = _CONTAINERALLOCATERESPONSE_ENVSENTRY
_CONTAINERALLOCATERESPONSE.fields_by_name['mounts'].message_type = _MOUNT
_CONTAINERALLOCATERESPONSE.fields_by_name['devices'].message_type = _DEVICESPEC
_CONTAINERALLOCATERESPONSE.fields_by_name['annotations'].message_type = _CONTAINERALLOCATERESPONSE_ANNOTATIONSENTRY
DESCRIPTOR.message_types_by_name['DevicePluginOptions'] = _DEVICEPLUGINOPTIONS
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['ListAndWatchResponse'] = _LISTANDWATCHRESPONSE
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['PreStartContainerRequest'] = _PRESTARTCONTAINERREQUEST
DESCRIPTOR.message_types_by_name['PreStartContainerResponse'] = _PRESTARTCONTAINERRESPONSE
DESCRIPTOR.message_types_by_name['AllocateRequest'] = _ALLOCATEREQUEST
DESCRIPTOR.message_types_by_name['ContainerAllocateRequest'] = _CONTAINERALLOCATEREQUEST
DESCRIPTOR.message_types_by_name['AllocateResponse'] = _ALLOCATERESPONSE
DESCRIPTOR.message_types_by_name['ContainerAllocateResponse'] = _CONTAINERALLOCATERESPONSE
DESCRIPTOR.message_types_by_name['Mount'] = _MOUNT
DESCRIPTOR.message_types_by_name['DeviceSpec'] = _DEVICESPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DevicePluginOptions = _reflection.GeneratedProtocolMessageType('DevicePluginOptions', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEPLUGINOPTIONS,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.DevicePluginOptions)
  })
_sym_db.RegisterMessage(DevicePluginOptions)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.Empty)
  })
_sym_db.RegisterMessage(Empty)

ListAndWatchResponse = _reflection.GeneratedProtocolMessageType('ListAndWatchResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTANDWATCHRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.ListAndWatchResponse)
  })
_sym_db.RegisterMessage(ListAndWatchResponse)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.Device)
  })
_sym_db.RegisterMessage(Device)

PreStartContainerRequest = _reflection.GeneratedProtocolMessageType('PreStartContainerRequest', (_message.Message,), {
  'DESCRIPTOR' : _PRESTARTCONTAINERREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.PreStartContainerRequest)
  })
_sym_db.RegisterMessage(PreStartContainerRequest)

PreStartContainerResponse = _reflection.GeneratedProtocolMessageType('PreStartContainerResponse', (_message.Message,), {
  'DESCRIPTOR' : _PRESTARTCONTAINERRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.PreStartContainerResponse)
  })
_sym_db.RegisterMessage(PreStartContainerResponse)

AllocateRequest = _reflection.GeneratedProtocolMessageType('AllocateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATEREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.AllocateRequest)
  })
_sym_db.RegisterMessage(AllocateRequest)

ContainerAllocateRequest = _reflection.GeneratedProtocolMessageType('ContainerAllocateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINERALLOCATEREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.ContainerAllocateRequest)
  })
_sym_db.RegisterMessage(ContainerAllocateRequest)

AllocateResponse = _reflection.GeneratedProtocolMessageType('AllocateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATERESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.AllocateResponse)
  })
_sym_db.RegisterMessage(AllocateResponse)

ContainerAllocateResponse = _reflection.GeneratedProtocolMessageType('ContainerAllocateResponse', (_message.Message,), {

  'EnvsEntry' : _reflection.GeneratedProtocolMessageType('EnvsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINERALLOCATERESPONSE_ENVSENTRY,
    '__module__' : 'api_pb2'
    # @@protoc_insertion_point(class_scope:v1beta1.ContainerAllocateResponse.EnvsEntry)
    })
  ,

  'AnnotationsEntry' : _reflection.GeneratedProtocolMessageType('AnnotationsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINERALLOCATERESPONSE_ANNOTATIONSENTRY,
    '__module__' : 'api_pb2'
    # @@protoc_insertion_point(class_scope:v1beta1.ContainerAllocateResponse.AnnotationsEntry)
    })
  ,
  'DESCRIPTOR' : _CONTAINERALLOCATERESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.ContainerAllocateResponse)
  })
_sym_db.RegisterMessage(ContainerAllocateResponse)
_sym_db.RegisterMessage(ContainerAllocateResponse.EnvsEntry)
_sym_db.RegisterMessage(ContainerAllocateResponse.AnnotationsEntry)

Mount = _reflection.GeneratedProtocolMessageType('Mount', (_message.Message,), {
  'DESCRIPTOR' : _MOUNT,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.Mount)
  })
_sym_db.RegisterMessage(Mount)

DeviceSpec = _reflection.GeneratedProtocolMessageType('DeviceSpec', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESPEC,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:v1beta1.DeviceSpec)
  })
_sym_db.RegisterMessage(DeviceSpec)


DESCRIPTOR._options = None
_CONTAINERALLOCATERESPONSE_ENVSENTRY._options = None
_CONTAINERALLOCATERESPONSE_ANNOTATIONSENTRY._options = None

_REGISTRATION = _descriptor.ServiceDescriptor(
  name='Registration',
  full_name='v1beta1.Registration',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1086,
  serialized_end=1156,
  methods=[
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='v1beta1.Registration.Register',
    index=0,
    containing_service=None,
    input_type=_REGISTERREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REGISTRATION)

DESCRIPTOR.services_by_name['Registration'] = _REGISTRATION


_DEVICEPLUGIN = _descriptor.ServiceDescriptor(
  name='DevicePlugin',
  full_name='v1beta1.DevicePlugin',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1159,
  serialized_end=1475,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetDevicePluginOptions',
    full_name='v1beta1.DevicePlugin.GetDevicePluginOptions',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_DEVICEPLUGINOPTIONS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListAndWatch',
    full_name='v1beta1.DevicePlugin.ListAndWatch',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_LISTANDWATCHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Allocate',
    full_name='v1beta1.DevicePlugin.Allocate',
    index=2,
    containing_service=None,
    input_type=_ALLOCATEREQUEST,
    output_type=_ALLOCATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PreStartContainer',
    full_name='v1beta1.DevicePlugin.PreStartContainer',
    index=3,
    containing_service=None,
    input_type=_PRESTARTCONTAINERREQUEST,
    output_type=_PRESTARTCONTAINERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEVICEPLUGIN)

DESCRIPTOR.services_by_name['DevicePlugin'] = _DEVICEPLUGIN

# @@protoc_insertion_point(module_scope)
