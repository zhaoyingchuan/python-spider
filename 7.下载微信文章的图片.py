# coding=utf-8
import re
import requests

def spider(paperurl, picpat):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    response = requests.get(paperurl, headers=headers).text

    pattern = re.compile(picpat)

    data = pattern.findall(response)

    for i in range(0, len(data)):
        picurl = data[i]
        print(picurl)
        write(picurl, i)


def write(picurl, i):
    data = requests.get(picurl).content
    with open("D:\Desktop\微信jpeg\\{}.jpeg".format(i), "wb") as f:
        f.write(data)


if __name__ == '__main__':
    paperurl = r"https://mp.weixin.qq.com/s/nR1ieFYsIqMXMx_BntUFEw"
    picpat = r'<img data-ratio="[\s\S]*?" data-src="(.*?)" data-type="jpeg" data-w="[\s\S]*?"'
    spider(paperurl, picpat)