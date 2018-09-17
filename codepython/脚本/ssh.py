import os
id = os.popen(r'docker run -dti --name dvwa --net=mynet --ip=172.16.70.11 citizenstig/dvwa:latest').read()
file = open('dvwa.txt','w+')
file.write(file[0:12])
file.close()