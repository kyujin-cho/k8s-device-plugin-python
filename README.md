# K8s Device Plugin implmenentation in Python

A simple stub definition for Kubernetes' Device Plugin implmenetation, written in Python.    
This repository is originated from CUDA Device Plugin for Backend.AI, with removing proprietary codes.

## Requirements
- Python 3.6 or above

## Installation
- Why are you trying to install this? 

## Development
### Setting up dependencies
Run 
```sh
python -c "import configparser; c = configparser.ConfigParser(); c.read('setup.cfg'); print(c['options']['install_requires'])" | xargs pip install
```

### Recompiling Protobuf Python codes
1. Run 
```sh
python -c "import configparser; c = configparser.ConfigParser(); c.read('setup.cfg'); print(c['options.extras_require']['build'])" | xargs pip install 
python -c "import configparser; c = configparser.ConfigParser(); c.read('setup.cfg'); print(c['options.extras_require']['dev'])" | xargs pip install
```
to install build-only dependencies.

2. Run `cd src/kyujin/deviceplugin/grpc`.
3. Run `python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. -I=$GOPATH/src -I=$GOPATH/src/github.com/gogo/protobuf/protobuf gogo.proto api.proto`.
