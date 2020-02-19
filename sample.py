#coding=utf-8
import re
import requests
from lxml import etree

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}
url = r"https://mp.weixin.qq.com/s/7huJOS7G4HEZYx1FtOTxIw"

response=requests.get(url,headers=headers).text


pat1=r'<img data-ratio="[\s\S]*?" data-src="(.*?)" data-type="jpeg" data-w="[\s\S]*?"'
pattern1=re.compile(pat1)
data1=pattern1.findall(response)
for i in range(0,len(data1)):
    picurl = data1[i]
    data = requests.get(picurl).content
    with open("D:\Desktop\微信jpeg\\{}.jpeg".format(i), "wb") as f:
        f.write(data)