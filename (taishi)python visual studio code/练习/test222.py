#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-15 11:45:57
# @Author  : Mr.zhang(s4ad0w.protonmail.com)
# @Link    : http://blog.csdn.net/csu_vc
import base64
import requests
import urllib
iv_raw='%2F8iEm4jh%2BjbgVGwlQ31ycg%3D%3D'  #这里填写第一次返回的iv值
cipher_raw='8WdhbPxjZy9xYAgoCeghiOUQu0ri1Y3dv7cX44MbvOfIC6zZxCbR%2FPFpeMatL5qIgT%2BYA66tIdCBpxtWsWxV9Q%3D%3D'  #这里填写第一次返回的cipher值
print "[*]原始iv和cipher"
print "iv_raw:  " + iv_raw
print "cipher_raw:  " + cipher_raw
print "[*]对cipher解码，进行反转"
cipher = base64.b64decode(urllib.unquote(cipher_raw))
#a:2:{s:8:"username";s:5:"zdmin";s:8:"password";s:5:"12345"}
#s:2:{s:8:"userna
#me";s:5:"zdmin";
#s:8:"password";s
#:3:"12345";}
xor_cipher = cipher[0:9] +  chr(ord(cipher[9]) ^ ord('m') ^ ord('a')) + cipher[10:]  #请根据你的输入自行更改，原理看上面的介绍
xor_cipher=urllib.quote(base64.b64encode(xor_cipher))
print "反转后的cipher：" + xor_cipher