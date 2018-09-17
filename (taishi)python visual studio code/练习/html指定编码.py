
import requests
import re
url = "http://lottery.sina.com.cn/"

xx = requests.get(url)
xx.encoding = 'UTF-8' #指定编码为utf-8
caipiao = re.findall(r'')
y = xx.text
print(y)
file = r"I:\python visual studio code\2.txt"
with open(file,'w+',encoding='utf-8') as f: #打开文件制定编码
    f.write(y)
    f.close()

