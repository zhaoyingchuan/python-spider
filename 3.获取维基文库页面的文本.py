#coding=utf-8

import requests
from lxml import etree

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}
url = r"https://zh.wikisource.org/wiki/脂硯齋重評石頭記/第三回"

response=requests.get(url,headers=headers).text

html=etree.HTML(response)

# title1=html.xpath("//div/table/tbody/tr/td/text()")
# print(title1[2])

result=html.xpath("//div/p/text()")

t = ''
for i in result:
    t=t+i
print(t)




