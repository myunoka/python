import threading
import queue
'''
queue介绍----queue是python中的标准库，俗称队列，可以直接import 引用，在python2.x中，模块名为Queue
在python中，多个线程之间的数据是共享的，多个线程进行数据交换的时候，不能够保证数据的安全
性和一致性，所以当多个线程需要进行数据交换的时候，队列就出现了，队列可以完美解决线程间的数据交换，保证线程间数据的安全性和一致性
'''
import time

thread = 10
password = queue.Queue()

fp = open(r'D:\codepython\线程\pwd.txt','r')
for i in fp:
     passwd = i.strip()#strip是去空格
     password.put(passwd)#把数据写入password列队里
     print(passwd)

#password.empty():::empty()如果为空就返回True，否则为false
#not 的意思就反过来 (如果为空就返回false。)

def buf():
    while not password.empty():#如果为空就返回false
        passworddata = password.get()#queue的get方法不会读取相同的值。因为get是读队列。也就是一列列的读数据
        print(time.ctime(),passworddata +'---------------')

for i in range(thread):
    t = threading.Thread(target=buf)
    t.start()
    t.join()

