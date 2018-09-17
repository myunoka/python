#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-15 11:45:57
# @Author  : Mr.zhang(s4ad0w.protonmail.com)
# @Link    : http://blog.csdn.net/csu_vc
import base64
import requests
import urllib.request
iv_raw='2vML9amot8cRR%2FcZA1lrJw%3D%3D'  #这里填写第一次返回的iv值
cipher_raw='BE4Jkuz8hdNI%2Fljzaq6%2BvQLHepCU5hKM0bq%2FWXWF6lrKbFxak9vAHwCjsDF53e094IiMuk%2FqSuMRlGRg8FCsOg%3D%3D'  #这里填写第一次返回的cipher值
print("[*]原始iv和cipher")
print("iv_raw:  " + iv_raw)
print("cipher_raw:  " + cipher_raw)
print("[*]对cipher解码，进行反转")
cipher = base64.b64decode(urllib.request.unquote(cipher_raw))
#a:2:{s:8:"username";s:5:"zdmin";s:8:"password";s:5:"12345"}
#s:2:{s:8:"userna
#me";s:5:"zdmin";
#s:8:"password";s
#:3:"12345";}
xor_cipher = cipher[0:9] +  chr(ord(cipher[9]) ^ ord('m') ^ ord('a')) + cipher[10:]  #请根据你的输入自行更改，原理看上面的介绍
xor_cipher=urllib.request.quote(base64.b64encode(xor_cipher))
print("反转后的cipher：" + xor_cipher)