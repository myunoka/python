#无参数装饰器
import time
def f1():
    print('the is f1')

# def cure(func):
#     print(time.time())
#     func()
# cure(f1)
def f2(func):
    def f3():
        print(time.time())
        func()
    return f3
f = f2(f1)
f()