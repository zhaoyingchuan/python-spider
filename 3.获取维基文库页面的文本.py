#coding=utf-8
import re
import requests

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}

response=requests.get(r"https://zh.wikisource.org/wiki/%E8%84%82%E7%A1%AF%E9%BD%8B%E9%87%8D%E8%A9%95%E7%9F%B3%E9%A0%AD%E8%A8%98",headers=headers).text

pat1=r'title="脂硯齋重評石頭記/(.*?)">第[\s\S]*?回</a>　[\s\S]*?</li>'
pat2=r'title="脂硯齋重評石頭記/第[\s\S]*?回">第[\s\S]*?回</a>　(.*?)</li>'

pattern1=re.compile(pat1)
pattern2=re.compile(pat2)

data1=pattern1.findall(response)
data2=pattern2.findall(response)


resultlist=[]
for i in range(0,len(data1)):
	# resultlist.append(data1[i]+data2[i])
    print(data1[i],data2[i])



