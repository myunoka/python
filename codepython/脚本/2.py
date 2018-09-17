import threading
import time

y = 11
def thread_job(x):
    print('T1 start\n')
    for i in range(10):
        time.sleep(1)
    print('T1 finish\n')
    print(x)
def main():
    added_thread = threading.Thread(target=thread_job, name='T1', args=(y,))
    added_thread.start()
    added_thread.join()
    print('all done\n')
    #print(threading.enumerate())
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())
if __name__ == '__main__':
    main()