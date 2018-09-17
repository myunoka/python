import re

xx = 'AjfnogjsgnnlBfjj l;jopgC'

c = re.findall('A(.*)B(.*)C', xx)
print(c)
cc = re.search('A(.*)B(.*)C', xx)
#group是返回结果
print(cc.group(0))#group默认是输出外面的大分组也是0
print(cc.group(1))
print(cc.group(2))
print(cc.groups())#groups默认只输出正则里面的分组不会输出外面的大分组