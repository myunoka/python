import socket

client = socket.socket()
ip = '120.79.40.131'
port = 5203
client.connect((ip, port))
data = input('please send:')

client.send('please:')
data_recv = client.recv(1024)
print(client_recv.decode())
client.close()