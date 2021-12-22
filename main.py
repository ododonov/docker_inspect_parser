import json
import os

path = "/var/python/docker_inspect_parser"
os.chdir(path)

json_file = "template.json"
with open(json_file, "r") as read_file:
    data = json.load(read_file)[0]

#General info about container
create_date = data["Created"]
container_state = data["State"]
container_status = container_state["Status"]

if(container_state["Running"]):
    container_status_color = '\033[92m'
elif(container_state["Paused"]):
    container_status_color = '\033[91m'
elif(container_state["Restarting"]):
    container_status_color = '\033[93m'
print('-----')
print('Created at', create_date)
print('Status:', container_status_color + container_status, '\033[0m')
print('-----')

#Volumes and ports
host_config = data["HostConfig"]

print('Volumes:')
binds = host_config["Binds"]
for i in range(len(binds)):
    print('- ', binds[i])
print('Ports:')
ports = host_config["PortBindings"]
#print(host_config["PortBindings"]["3000/tcp"][0]["HostPort"])

for i in ports:
    container_port = i
    host_port = ports[i][0]["HostIp"] + ':' + ports[i][0]["HostPort"]
    print('- ', container_port, ' : ', host_port)
