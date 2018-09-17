import telnetlib
import time
def telnet(tnip):
    demo = telnetlib.Telnet(tnip, timeout=30)
    demo.set_debuglevel(0)
    z = demo.read_until(b'Password:')
    print(z)
    time.sleep(3)
    #paw = open('paw.txt')
    #paw = paw.readline()
    paw =  'NoobsX@x4z2x8%**'
    c = demo.write((paw + '\r\n').encode('ascii'))
    print(c)
    time.sleep(3)
    demo.read_until(fin.encode('ascii'))
    demo.write(('dis access-user' + '\n').encode('ascii'))
    # x = str(demo.read_some())
    # print(x)
    x = demo.read_until(fin.encode('ascii'))
    file = r'D:\codepython\脚本\user1.txt'
    with open(file,'w+',encoding='utf-8') as f: #打开文件并且设置指定utf-8编码
        f.write(str(x))
        f.close()
    demo.close()
if __name__ == '__main__':
    fin = '<'
    ip = '10.2.0.4'
    telnet(ip)    
