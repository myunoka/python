import re
#match和search函数匹配到第一个字符就停止
xx = '1B279C3D47'

c = re.match('\d', xx)#match函数只会匹配字符串第一个字符并且返回结果
print(c.span())#.span可以返回位置
cc = re.search('\d', xx)#search会匹配整个字符串符合正则的要求，并且停止
print(cc.group())#.group返回结果
ccc = re.findall('\d', xx)
print(ccc)