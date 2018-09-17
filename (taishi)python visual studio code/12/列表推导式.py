# 列表推导式
# 集合推导式
# set、dict、元组 都可以被推倒

a = [1,2,3,4,5,6]
#列表推导式
b = [i*i for i in a]

#列表推导式(加判断语句)
c = [i*i for i in a if i > 5]
print(c)

#字典列表推导式
d = {
    '小明' : 17,
    '小红' : 18,
    '小丽' : 19
}
f = [key for key in d]
g = {value:key for key,value in d}
#print(g)
h = (key for key,value in d.items())
for i in h:
    print(i)
