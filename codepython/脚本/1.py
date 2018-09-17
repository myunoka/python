# try:
#     for i in range(5):
#         print(i)
#         break
#     else:
#         print('结束')
# except:
#     pass

# else:
#     print('w')
# finally:
#     print('hah')
# cc = {'q':11,'w':22}
# cc['e']=33
# print(cc['q'])
# print(cc)
# for key in cc:
#     print(cc[key])
# class People(object):
#     #类变量可以由所有的对象访问，但是对象只能访问，不能修改
#     #可以用来做资源共享
#     total=0
#     name = 'python 8期'
#     #初始化函数，添加对象属性
#     def __init__(self,name,age,school):
#         #给对象属性赋值
#         self.name=name
#         self.age=age
#         self.school=school
#         #只能使用类去修改
        
#         People.total+=1
#         print(People.name)

    
# p1=People('张三',21,'**大学')
# print(p1.total)
# p2=People('钊冉',22,'***大学')

# print(p2.total)

class com():
    xxx = 1
    print(xxx)
x = com()
x.xxx = 2
print(x.xxx)

