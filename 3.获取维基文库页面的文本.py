#coding=utf-8

import requests
from lxml import etree

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}
url = r"https://zh.wikisource.org/wiki/%E8%84%82%E7%A1%AF%E9%BD%8B%E9%87%8D%E8%A9%95%E7%9F%B3%E9%A0%AD%E8%A8%98/%E7%AC%AC%E4%B8%80%E5%9B%9E"

response=requests.get(url,headers=headers).text

html=etree.HTML(response)

# title1=html.xpath("//div/table/tbody/tr/td/text()")
# print(title1[2])

result=html.xpath("//div/p/text()")

t = ''
for i in result:
    t=t+i
print(t)




