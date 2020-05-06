# coding=utf-8
import re
import requests
from lxml import etree
from lxml import html

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}

url = r"https://mp.weixin.qq.com/s?__biz=MzA3MjgyNDIyNw==&mid=2652609820&idx=4&sn=5a2b108bd97d52be477bc10bbe42bcc2&chksm=84f759d0b380d0c6d4749aa7b4b90bf04500a76d9426334c0524c339e0df22e4525020cdb89e&scene=27#wechat_redirect"

response = requests.get(url, headers=headers).text

# print(response)

pat = r'<img data-ratio="[\s\S]*?" data-src="(.*?)" data-type="jpeg" data-w="[\s\S]*?"'

pattern = re.compile(pat)

data = pattern.findall(response)

for i in range(0, len(data)):
    picurl = data[i]
    print(picurl)
    data = requests.get(picurl).content
    with open("D:\Desktop\微信jpeg\\{}.jpeg".format(i), "wb") as f:
        f.write(data)
