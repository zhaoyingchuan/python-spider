#import urllib.request
from urllib import request

url=r"https://zh.wikisource.org/wiki/脂硯齋重評石頭記/第十三回"

#发送请求.获取响应信息
reponse=request.urlopen(url).read()


print(type(reponse))

