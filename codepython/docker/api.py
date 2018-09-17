import docker
import sys
client = docker.DockerClient(base_url='tcp://172.16.70.10:2375', version='auto')
# client.containers.run('dvwa',command=/bin/bash)
client.stop('7bb35e70d1ab')

#client.containers.run("ubuntu:16.04" , " ","-dti --net=mynet --ip=172.16.70.19")
#sys.exit()


# #c = docker.Client(base_url='tcp://192.168.1.22:2375',version='1.14',timeout=10)  
# r=client.start(container='ubuntu:16.04', binds={'/data':{'bind': '/data','ro': False}}, port_bindings={80:80,22:2022}, lxc_conf=None,  
#         publish_all_ports=True, links=None, privileged=False,  
#         dns=None, dns_search=None, volumes_from=None, network_mode=None,  
#         restart_policy=None, cap_add=None, cap_drop=None)  
# #通过start方法启动容器，指定数据卷的挂载关系及权限，以及端口与主宿机的映射关系等  
# print(str(r))