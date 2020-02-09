# coding=utf-8

import requests
from lxml import etree
import time

class Spider(object):
    def __init__(self):
        self.url = "https://zh.wikisource.org/zh-hans/"
        self.header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

    # 构造url
    def tiebaSpider(self):
        url = r"https://zh.wikisource.org/zh-hans/脂硯齋重評石頭記"
        response = requests.get(url, headers=self.header).text
        html = etree.HTML(response)
        hreflist = html.xpath("//div/ul/li/a/@href")
        for href in hreflist:
            href = href.replace("/wiki/", "")
            myurl = self.url + href
            self.loadPage(myurl)

    # 爬取页面内容
    def loadPage(self, url):
        response = requests.get(url, headers=self.header).text
        html = etree.HTML(response)
        self.loadText(html)

    # 获取页面正文
    def loadText(self, html):
        result = html.xpath("//div/p/text()")
        text = ''
        for i in result:
            text = text + i
        # print(text)
        self.writeText(text)
        # time.sleep(10)

    # 保存正文到本地
    def writeText(self, text):
        f1 = open(r"D:\Desktop\脂砚斋重评红楼梦.txt", "a+",encoding='utf-8')
        f1.write(text)
        f1.close()


if __name__ == '__main__':
    mySpider = Spider()

    mySpider.tiebaSpider()
