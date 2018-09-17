import re

# xx = 'aqweqweqeqb111233c'

# xx = re.findall('a(\S*)b(\S*)c', xx)
# print(xx[0])

xx = ['a','b','d','c','f']
x = {'a':1,'c':3,'d':2}
yy = sorted(x.items(),key = lambda itme:itme[1])#itmek可以取key的key值和vlue值然后排序，，key参数是一个函数，用来取参与比较的元素
#注意排序后的返回值是一个list，而原字典中的名值对被转换为了list中的元组。
#直接使用sorted(yy.keys())就能按key值对字典排序
#如果想按照倒序排序的话，则只要将reverse置为true即可。
#yy = sorted(xx)
print(yy)