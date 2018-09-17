#threading.clok 就是锁去锁定资源。就是某个资源现在只能在某个线程使用直至线程结束

import threading

def job1():
    global A, lock
    lock.acquire()#开始锁
    for i in range(10):##中间这一块语句就是你在运行这个lock的时候，job2线程是不会接触到job1的语句
        A += 1
        print('job1', A)
    lock.release()#解除锁
def job2():#job2使用lock也是一样的意思。。就是线程互不干涉。然后资源锁定
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2', A)
    lock.release()

def main():
    global A, lock
    A = 0
    lock = threading.Lock()
    t1 = threading.Thread(target=job1, name=job1)
    t2 = threading.Thread(target=job2, name=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()