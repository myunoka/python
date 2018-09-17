from selenium import webdriver
import time

def login():
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
    for i in pfile:
        flag.send_keys(str(i[4:-1]))
        tijiao = dr.find_element_by_id('btn_submit')
        tijiao.click()
        time.sleep(2)
    time.sleep(1950)
if __name__ == '__main__':
        login()
        
#try捕抓错误异常
# def temp_convert(var):
#     try:
#         return int(var)
#     except Exception as e:#输出错误异常
#         print('wwww', e)

# # 调用函数
# temp_convert("xyz")

