import json
import os

path = os.environ['DIP_HOME']
os.chdir(path)

json_file = (os.environ['DIP_RESULT'])
data = json.loads(json_file)[0]

## General info about container
container_state = data["State"]
container_status = container_state["Status"]
create_date = data["Created"]
container_name = data["Name"]

## Host config
host_config = data["HostConfig"]
#Volumes and ports
if "Binds" in host_config:
    binds = host_config["Binds"]
else:
    binds = None
if "PortBindings" in host_config:
    ports = host_config["PortBindings"]
else:
    ports = None

## Container config
container_config = data["Config"]
#Image
container_image = container_config["Image"]
#Environment
if "Env" in container_config:
    envs = container_config["Env"]
else:
    envs = None

## Networks
network_settings = data["NetworkSettings"]
networks = network_settings["Networks"]


## Print information
if(container_state["Running"]):
    container_status_color = '\033[92m'
elif(container_state["Paused"]):
    container_status_color = '\033[91m'
elif(container_state["Restarting"]):
    container_status_color = '\033[93m'
else:
    container_status_color = '\033[0m'
print('Name:', container_name[1:])
print('Image:', container_image)
print('Created at', create_date)
print('Status:', container_status_color + container_status, '\033[0m')

print('-----')

if(binds):
    print('Volumes (H:C):')
    for i in range(len(binds)):
        print('- ', binds[i])
else:
    print('Volumes: none')

if(ports):
    print('Ports (H:C):')
    for i in ports:
        container_port = i
        host_port = ports[i][0]["HostPort"]
        print('- ', host_port, ':', container_port)
else:
    print('Ports: none')

print('Networks:')
for i in networks:
    print('- ', i)

if(envs):
    print('Environment:')
    for i in range(len(envs)):
        print('- ', envs[i])
else:
    print('Environment: none')
