import requests
import re

def pc():
    url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=sublimetext3%20%E4%BB%A3%E7%A0%81%E8%A1%A5%E5%85%A8%E6%8F%92%E4%BB%B6&oq=sublimetext%2526lt%253B%2520%25E4%25B8%25BB%25E9%25A2%2598&rsv_pq=dfd97f2800007869&rsv_t=d4ebE1%2BFeVftYqj6Z9R7BgHKSaJeoYnSwuXNr4DIkdZhDsFETl6YRykCoI0&rqlang=cn&rsv_enter=1&rsv_sug3=53&rsv_sug2=0&inputT=11866&rsv_sug4=12080&rsv_jmp=slow'
    xinxi = requests.get(url)
    x