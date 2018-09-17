from socket import *
from time 
import os
HOST = "127.0.0.1"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
 
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
 
while True:
    print("waiting for connection...")
    tcpCliSock, addr = tcpSerSock.accept()
    print(tcpCliSock)
    print("connected from :", addr)
 
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        content = time.ctime(), data
        strdata = data.decode()
        print(strdata)
        print(type(strdata))
        print(content)
        print(type(content))
        tcpCliSock.send(content.encode("utf-8"))
 
    tcpCliSock.close()
 
tcpSerSock.close()
