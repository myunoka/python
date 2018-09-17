import re
file = r'D:\codepython\脚本\user1.txt'
with open(file, 'r+') as f:
    x = f.read()
    f.close()

jh = re.findall(r'812(.*)828', x)
print(jh)