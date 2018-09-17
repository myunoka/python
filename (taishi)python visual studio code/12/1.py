import re

import requests

url = 'https://www.douyu.com/g_LOL'
regular1 = '<span class="dy-name ellipsis fl">([\s\S]*?)</span>'
regular2 = '<span class="dy-num fr">([\s\S]*?)</span>'
s = '<p>([\s\S]*?)</p>'
x = '<span class="dy-name ellipsis fl">([\s\S]*?)</span>'
xx = '<span class="dy-num fr"  >([\s\S]*?)</span>'
r = requests.get(url)
r.encoding = 'utf-8'
html = r.text
f = re.findall(s, html)
anchors = []
for i in f:
    name = re.findall(x, i)
    name = "".join(name)
    number = re.findall(xx, i)
    number = "".join(number)
    anchor = {'name':name, 'number':number}
    anchors.append(anchor)
newlist = sorted(anchors, key=lambda k: k['number'], reverse=True)
#anchors2 = sorted(anchors)
#anchors1 = sorted(anchors, key=anchors2)
#anchors2 = sorted(anchors, key=anchors1)
#u = lambda k: k['number']
#r = re.findall('\d*',)
for i in newlist:
    print(i['name'] + '--------' + i['number'])
#print(anchors[0])
#print(newlist)