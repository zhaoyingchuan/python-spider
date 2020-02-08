# coding=utf-8
import re
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}
url = r"https://zh.wikisource.org/zh-hans/脂硯齋重評石頭記"

response = requests.get(url, headers=headers).text

html = etree.HTML(response)

result1=html.xpath("//li/a/@title") #获取所有span标签的信息
result2 = html.xpath("//li/text()")  # 获取所有span标签的信息

for i in range(0, len(result2)):
    print(result1[i]+result2[i])
