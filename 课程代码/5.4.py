#获取一类标签
from lxml import etree

html=etree.parse(r"D:\Desktop\python爬虫教程\课程代码\hello.html")

result=html.xpath("//a") #获取所有span标签的信息

for i in result:
    print(i.text)

