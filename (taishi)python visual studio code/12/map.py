#map() 会根据提供的函数对指定序列做映射。
#第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
#相当于一个for循环
#结果为列表
list_x = [1,2,3,4,5]
list_y = [1,2,3,4,5]
def s(x):
    return x*x

#f = map(s, list_x)#使用正常函数
#print(list(f))

f = map(lambda x, y: x*x, list_x, list_y)#使用lambda匿名函数
print(list(f))