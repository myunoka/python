#结果为集合
#filter过滤器
list_x = [1,2,0,1,0,1]
list_y = ['a','A','b','B']
f = filter(lambda x: True if x.isupper()==True else False, list_y)#判断大小写
#f = filter(lambda x: x, list_x)#filter 表达式(函数表达式)必须是可以返回布尔类型的结果(也就是true或者false)
print(list(f))

    