import requests
import time

while True:
    file = open(r'I:\python visual studio code\ctf\flag.txt','r+')
    file1 = file.readlines()
    for i in file1:

        url1 = 'https://172.16.223.202/match/WAR16/oapi?atn=answers&token=PYHWMWAX&flag='+str(i[4:-1])
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer' :  'http://172.16.223.104/index.php?action=view&mod=index',
            'Cookie' : 'php-console-server=5; matchToken_16=eyJpdiI6ImRPb3NjTFI3OCtWaXVnaXBESklNN2c9PSIsInZhbHVlIjoiTkFrUHpPcFRMeUpcL1wvRE1tUWxaa3pWamYxMWsrUkt3cmxTV082NE5Na094M2pScWRobytxNStmK29yZ0F6NnZRdGNUbTlaT0RJUjZmT21VdUZSSEorQ1I3RXd6MStiOE0yXC9CVlZ2blhJTm9GVzl0ZzRUa1N6aVJteDlxYjJKTE8iLCJtYWMiOiIwM2IzYjc1NDVmMjhmZDk5NjNmZWY5ZDc4NWI1Y2U0NWExNDMyYmM0ODdjYThiNjZjNjhiZjY0ZDk2MThlYjVjIn0%3D; adl=eyJpdiI6ImpvZWlSd01PZjNmVGpLUzNKWW1Cemc9PSIsInZhbHVlIjoicE9Td1M0cStjZFB0SHJ4RWQ1WVVDeHJLQTRTS0VEenltOGJZeGQ5TkxcL3RRYm5HbklLbUtcL2toRklkOUphYTdJN3djTFFncTYrbGEzUFNsUGNIckd0dz09IiwibWFjIjoiNTE1OTQ4MDY1NDJkNmVhMzJhYTU3MTIyNDhkOGEyMDY1Yzk3NWEyYjJkMzI0YTkyY2RhMWNiNTQ3NTU2YzE3NSJ9'
    
        }
    time.sleep(2000)
#xx = requests.get(url, headers=headers, verify=False).text

#print(xx)

