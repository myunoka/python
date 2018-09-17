import docker
client = docker.APIClient(base_url='tcp://172.16.70.10:2375',version='auto',timeout=10)
xinxi = client.version()
print(xinxi)