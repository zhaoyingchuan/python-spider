# coding=utf-8
import re
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}
url = r"https://zh.wikisource.org/wiki/脂硯齋重評石頭記"

response = requests.get(url, headers=headers).text

# html = etree.HTML(response)
#
# result1=html.xpath("//li/a/@title") #获取所有span标签的信息
# result2 = html.xpath("//li/text()")  # 获取所有span标签的信息
#
# for i in range(0, len(result2)):
#     print(result1[i]+result2[i])

pat1=r'title="脂砚斋重评石头记/(.*?)">第[\s\S]*?回</a>　[\s\S]*?</li>'
pat2=r'title="脂砚斋重评石头记/第[\s\S]*?回">第[\s\S]*?回</a>　(.*?)</li>'

pattern1=re.compile(pat1)
pattern2=re.compile(pat2)

data1=pattern1.findall(response)
data2=pattern2.findall(response)


resultlist=[]
for i in range(0,len(data1)):
	# resultlist.append(data1[i]+data2[i])
    print(data1[i],data2[i])