import requests
import re

class Spider():

    url = 'http://xy7966.com'
    history = 'https://xy7966.com/#detailNumbers?lottery_id=23'
    history1 = '<div class="red null">([\s\S]*?)</div>'
    def __request(self):
        f = requests.get(Spider.history1)
        f.encoding = 'utf-8'
        html = f.text
        
        return html

    def go(self):
        htmls = self.__request()
        print(htmls)

spider = Spider()
spider.go()