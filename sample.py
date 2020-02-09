# coding=utf-8
import requests
from lxml import etree

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}

# 爬取页面内容
def loadPage(url):

    response = requests.get(url, headers=headers).text

    html = etree.HTML(response)

    result = html.xpath("//div/p/text()")

    t = ''
    for i in result:
        t = t + i

print(t)

if __name__ == '__main__':

    url=input("请输入：")

