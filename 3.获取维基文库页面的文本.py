#coding=utf-8

import requests
from lxml import etree

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}
url = r"https://zh.wikisource.org/zh-hans/三國演義/第003回"

response=requests.get(url,headers=headers).text

html=etree.HTML(response)

# title1=html.xpath("//div/table/tbody/tr/td/text()")
# print(title1[2])

title1 = html.xpath("//div/table/tbody/tr/td/text()")
title2 = html.xpath("//div/table/tbody/tr/td/b/text()")
result=html.xpath("//div/p/text()")

text = ''
for i in result:
    text=text+i

all = title1[4] + title2[1] + text

print(all)





