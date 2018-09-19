from multiprocessing import Process
import time

class mynewProcess(Process):
    def run(self):
        while True:
            print('----1----')
            time.sleep(1)
p = mynewProcess()
p.start()
while True:
     print('----2----')
     time.sleep(1)
