#coding=utf-8

import requests
from lxml import etree

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}

url = r"https://zh.wikisource.org/zh-hans/三國演義"

response=requests.get(url,headers=headers).text

print(response)

html=etree.HTML(response)

hreflist=html.xpath("//div/ul/li/a/@href")
# del hreflist[0:2]
for href in hreflist:
    href=href.replace("/wiki/", "")
    print('https://zh.wikisource.org/zh-hans/'+ href)

# result=html.xpath("//div/p/text()")
#
# t = ''
# for i in result:
#     t=t+i
# print(t)
