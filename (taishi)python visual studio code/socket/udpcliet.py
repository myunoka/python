import threading
from socket import *

def recvdata():
	while True:
		recvinfo = udpsocket.recvfrom(1024)
		print('>>%s:%s'%(str(recvinfo[1]),recvinfo[0]))

def senddata():
	while True:
		sendinfo = input('<<')
		udpsocket.sendto(sendinfo.encode('gb2312'), (destip,destport))

udpsocket = None
destip = ''
destport = 0

def main():
	global udpsocket, destport, destip
	destip = input('对方的ip：')
	destport = int(input('对方的port:'))
	localport = int(input('本地的port:'))

	udpsocket = socket(AF_INET, SOCK_DGRAM)
	udpsocket.bind(('', localport))

	tr = threading.Thread(target=recvdata)
	ts = threading.Thread(target=senddata)

	tr.start()
	ts.start()

	tr.join()
	ts.join()
	
if __name__ == '__main__':
	main()