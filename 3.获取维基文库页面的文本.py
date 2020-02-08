#coding=utf-8
import re
import requests
from lxml import etree


headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}
url = r"https://zh.wikisource.org/zh-hans/脂硯齋重評石頭記/第二十二回"

response=requests.get(url,headers=headers).text

html=etree.HTML(response)

result=html.xpath("//div/p/text()") #获取所有span标签的信息
# print(result)
t = ''
for i in result:
    t=t+i
print(t)




