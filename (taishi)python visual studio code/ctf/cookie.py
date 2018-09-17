import requests
import time
while True:
    x = [120,121,122,123,124,125,126,127,128,129,130,132,133,134,135,137,138,139]
    for i in x:
        url = 'http://172.16.223.'+str(i)+'/index.php?r=admin'
        url1 = 'http://172.16.223.'+str(i)+'/index.php?r=admin/dbback/sqlrun'   
        print(url)
        print(url1)
        
    time.sleep(1800)