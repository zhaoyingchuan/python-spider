#coding=utf-8
import re
import requests
from lxml import etree


headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}
url = r"https://zh.wikisource.org/zh-hans/脂硯齋重評石頭記/第九回"

response=requests.get(url,headers=headers).text

html=etree.HTML(response)

result=html.xpath("//div/p/text()") #获取所有span标签的信息
# print(result)
t = ''
for i in result:
    t=t+i
print(t)
# pat1=r'title="脂硯齋重評石頭記/(.*?)">第[\s\S]*?回</a>　[\s\S]*?</li>'
# pat2=r'title="脂硯齋重評石頭記/第[\s\S]*?回">第[\s\S]*?回</a>　(.*?)</li>'
#
# pattern1=re.compile(pat1)
# pattern2=re.compile(pat2)
#
# data1=pattern1.findall(response)
# data2=pattern2.findall(response)
#
#
# resultlist=[]
# for i in range(0,len(data1)):
# 	# resultlist.append(data1[i]+data2[i])
#     print(data1[i],data2[i])



