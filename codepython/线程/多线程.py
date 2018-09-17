#只有函数或者类才能运用多线程
#函数启动是由线程函数调用的
import threading
import time
def f(i):
    print('I am from a thread, num = %d \n' %(i))
    print(time.ctime())

def main():
    for i in range(1,10):#for循环创建10子线程
        t = threading.Thread(target=f,args=(i,))#这里i为什么需要加个‘，’号呢，因为参数列表至少为两个这里加个‘，’表示两个参数，但是第二个为空
        t.setDaemon(True)#设置子线程为守护线程 注意：必须在运行线程之前被调用   
        #当我们使用setDaemon(True)方法，设置子线程为守护线程时，主线程一旦执行结束，
        # 则全部线程全部被终止执行，可能出现的情况就是，子线程的任务还没有完全执行结束，就被迫停止
        t.start()#启动线程
    t.join()#阻塞进程直到线程执行完毕   进程在所有线程结束后才退出
    #join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程在终止
    #join ()方法：主线程A中，创建了子线程B，并且在主线程A中调用了B.join()，那么，主线程A会在调用的地方等待，直到子线程B完成操作后，
    # 才可以接着往下执行，那么在调用这个线程时可以使用被调用线程的join方法。
    print('主线程结束')
if __name__ == '__main__':
    main()#主线程