from functools import reduce

#连续计算，连续调用lambda
#结果为数值
list_x = [1,2,3,4,5]

f = reduce(lambda x, y: x+y, list_x)
print(type(f))
print(f)
#计算过程是。首先我们定义lambda函数是两个参数。但是运行时reduce会重参数(list_x)里面调用两个参数值作为x,y。然后计算结果在赋值给x参数,然后重参数里面调用第三个参数值并且赋值给y。一直连续到结束，返回结果
# (((1+2)+3)+)+5

list_a = [(1,3),(2,-2),(-2,3)]
f = reduce(lambda x, y:x+y, list_a)
print(f)    
a = ((1,2)+(2,-2))
print(a)
print(type(a))
