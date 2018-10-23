#有参数装饰器
import time

def f2(func):
    def f3(*args):#args可变参数(可以接收多个参数)
        print(time.time())
        func(*args)
    return f3
#流程 # 调用@f2然后把f1当成f2的参数传入，并且赋值给f1。然后f2把f3返回来，然后调用f1()相当执行了f3()。
#装饰器 每一层指向的都是下一层
@f2#相当于 f1 = f2(f1)(这里是需要传入的参数是在调用装饰器的下一层这里也是就是f1)由于f2()是一个decorator，返回一个函数，所以，原来的f1()函数仍然存在，只是现在同名的f1变量指向了新的函数，于是调用f1()将执行新函数，即在f2()函数中返回的f3()函数
def f1(fun_name):
    print('the is f1'+fun_name)
f1('test')


@f2
def f4(fun_name1,fun_name2):
    print('the is f1'+fun_name1,fun_name2)

f4('test1','test2')
