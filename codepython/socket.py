from socket import *

demo = socket(AF_INET, SOCK_STREAM)
demo.sendto(b'the is test', ('192.168.150.130', '6300'))
demo.close()
