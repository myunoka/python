import multiprocessing
import time

def func(msg):
    print(multiprocessing.current_process().name + '-' + msg + '---' + time.ctime())

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4) # 创建4个进程
    for i in range(50):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg, ))#apply_async主进程不堵塞（apply主进程堵塞直到所有子进程完全才继续执行）
    print("Sub-process(es) done.")
    pool.close() # 关闭进程池，表示不能在往进程池中添加进程
    pool.join() # 等待进程池中的所有进程执行完毕，必须在close()之后调用
    