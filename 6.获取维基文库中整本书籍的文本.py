# coding=utf-8

import requests
from lxml import etree

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
        result = html.xpath("//div/p/text()")
        t = ''
        for i in result:
            t = t + i
        print(t)

    # 获取页面正文
    def loadText(self, link):
        pass

    # 保存正文到本地
    def writeText(self, text):
        pass


if __name__ == '__main__':
    mySpider = Spider()

    mySpider.tiebaSpider()
