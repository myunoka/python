import re
import requests

class Spider():
    url = 'https://www.douyu.com/g_LOL'
    regular1 = '<p>([\s\S]*?)</p>'
    regular2 = '<span class="dy-name ellipsis fl">([\s\S]*?)</span>'
    regular3 = '<span class="dy-num fr"  >([\s\S]*?)</span>'

    def __request(self):
        r = requests.get(Spider.url)
        r.encoding = 'utf-8'
        htmls = r.text

        return htmls

    def __Analysis(self, htmls):
        anchors = []
        f = re.findall(Spider.regular1, htmls)
        for anchor in f:
            name = re.findall(Spider.regular2, anchor)
            name = "".join(name)
            number = re.findall(Spider.regular3, anchor)
            number = "".join(number)
            anchor = {'name':name, 'number':number}
            print(anchor)
            anchors.append(anchor)    
        return anchors

    def __sort(self, anchor):
        newlist = sorted(anchor, key=lambda k: k['number'], reverse=True)
        return newlist

    def __show(self, anchor):
        for i in anchor:
            print(i['name'] + '--------' + i['number'])

    def go(self):
        htmls = self.__request()
        anchors = self.__Analysis(htmls)
        anchor = self.__sort(anchors)
        self.__show(anchor)


spider = Spider()
spider.go()