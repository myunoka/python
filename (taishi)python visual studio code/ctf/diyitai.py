import os
import time
while True:
    yyy = open('/opt/flag.txt', 'a+')
    for x in range(101,112):
        url = os.popen('curl http://172.16.223.'+str(x)+'/images/avatar/0.jpg').read()
        yyy.write(str(x)+':'+str(url)+'/\n')
        yyy.close()
    time.sleep(1800)
    yyy.write('新的一轮开始','w+')

