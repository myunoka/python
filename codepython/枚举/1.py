from enum import Enum
#枚举类型、枚举名字、枚举值
class vip(Enum):
    com = 1
    com1 = 1 #在枚举里数值相同的只有第一个是枚举的类型，第一个数值相同的是别名。也就是第一个跟他相同数值的类型的别名
    cn = 2
    ci = 3

# print(type(vip.com))#输出的是枚举类
# print(vip.com.value)#输出的是枚举的值
# print(type(vip.com.name))#输出的是枚举的名字

#正常遍历枚举的类型时别名是不在遍历里面的
# for v in vip:#遍历获得枚举下的每个枚举的类型
#     print(v)
#运算符比较
#枚举只支持==和is运算符比较
#枚举可以身份和等值比较、不能大小比较

#正常遍历枚举的类型时别名是不在遍历里面的
#遍历枚举别名方法如下：
# for v in vip.__members__:
#     print(v)

#   枚举转换（如何把一个数值转换为枚举类）
# a = 1
# print(vip(a))#这样就简单的把数字1转换成枚举vip里面的com了。（这并不是真正的转换）
# vv = vip.com == vip.cn
# vi = vip.com is vip.com
# print(vv)
# print(vi)