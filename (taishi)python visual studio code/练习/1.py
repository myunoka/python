import requests
import time
while True:
    file = open(r'I:\python visual studio code\ctf\flag.txt', 'r')
    lins = file.readlines()
    for i in lins:
        url = 'https://172.16.223.202/match/WAR15/api'
        headers = {
            'Accept' : 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language' : 'zh-CN,zh;q=0.9',
            'Connection' : 'keep-alive',
            'Content-Length' : '84',
            'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie' : 'php-console-server=5; token=eyJpdiI6Im1pTUFUNDVnb2VsdGY0ZklSMXRHa3c9PSIsInZhbHVlIjoiVWxwYjlQOXlUS2RwemVyWXdhSDRhd0VNTTllXC9yNjdLK1RPbmNVcVYzaDRMZWx3XC9JNWt4cmdDXC9wT0JGVGtiS1VLVlBoUWdaM2FHSEVcL1Uzcm5YTHlidlZKSVdEaldEa1wvdFgrbmNkcXdkUT0iLCJtYWMiOiI0ZTFlNWU4MTFlNGRlNzY3ZjUzNTNlOTE2MzFhZGYyOWI3ZGU3YjliODViM2ZmYjEyMTFlMmFmZjNkODIzOTlkIn0%3D; matchToken_15=eyJpdiI6IjBcL1hIS3JveE8wbldFRnBOXC9qMk4zQT09IiwidmFsdWUiOiJNQnk1b05aWUVETENXUjJPb1ZQYmxHS3hPWTd0ZFlXdGZ3eEYyWkdcL1Qrc1Rod2ZDQWdXWmlLT09RQ0hJa0tPTmhrTU16YWk3SzJ4aHBlckIrRENYTjFBMzVDeGE2OWxuTHpxMWE2RnYwS1llQUpcL29HVVhpY2NkeWtOV3VhWDRFIiwibWFjIjoiZDRhOWQyOWU4MzAyOTYwZWNlNmNlYzJkN2RkYTY1MzA1OWEzOTZlZGI0ODFkNWIxZWQzYjFhYjlmOTA2MDY3OCJ9; matchToken_16=eyJpdiI6Im5mVkZtOGxCXC85RDNaTStlbzdDUkhRPT0iLCJ2YWx1ZSI6IktqYU9jT0xaRFJsQlRZQUdPUXUwcVdVYTlWQWVpTlQrNXFYMmRmWmoraDVDUEFrRkExYVFVWGdCeFBQbGptNnYzZFAxV3ZLRm5XOGhYMks3ZE9sSGxyblJKUitQcEQrVDMyakxudmpwRnRmUklXbDVSMGFBcUJCVld1aHVEdUpKIiwibWFjIjoiYjBmYzk2YjY1MzQ3YTc0MzU4MDY4NWFmNjMxYmQzOGJmYmUwOGE0NjJkMmY4NDEzZTA0NGQ2OGFiNTEyZGEyMSJ9; adl=eyJpdiI6ImpvYlNZOGNJVFBieTgxRkVQNzBoQmc9PSIsInZhbHVlIjoiXC9zbitIc2dZdGVtWm4xM0ZWcmJnQTFcL1I4ZDZ3c3dINW1XcitWR1R4dmsrVDdpRzBjSUo1UmlYc3BUUkNPeDB0R25BbHQ3SDZQYWlDMHhEWWZ6UmtaUT09IiwibWFjIjoiY2ZkNmY2YWEzNTc4YTdkODQ5NjFiNjJjZTA4ZTUxNTZiNGI5NWMyYThhYzY2ZWE1OTFmNTZlNzY4OGU5MDIzNSJ9',
            
            'Host' : '172.16.223.202',
            'Origin' : 'https://172.16.223.202',
            'Referer' : 'https://172.16.223.202/match/WAR16/entry',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'X-CSRF-TOKEN' : 'e3EWGFsYBqBeXrfYkwwvDdTfeBx31iGQ7gg2jQT',
            'X-Requested-With' : 'MLHttpRequest'
            }
        data = {
           'atn' : 'answers',
           'id' : '7',
#           'token' : 'LB2GrfskKgP3k3kA42b_16',
           'flag' : str(i[4:-1])
            }
        xx = requests.post(url, headers=headers, data=data, verify=False).text
        print(xx)
        print(str(i[:3]))
    time.sleep(1900)
