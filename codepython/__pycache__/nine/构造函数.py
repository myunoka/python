class demo():
    name = ' '
    age = 10
#'类变量' '实例变量'
    def __init__(self,name, age):#构造函数是自动调用运行的
        #构造函数
        #初始化对象的属性
        name = name 
        age = age
        # print('demo')
        #构造函数只能返回None
    def demo3(self):
        print(self.age)
demo1 = demo('xisxis',20)#实例化 调用demo类
print(demo1.name)
# demo1.demo3()#调用类里面的方法
# demo1.__init__()

