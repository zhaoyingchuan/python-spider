#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import HTTPError
try:
    html = urlopen("https://zh.wikipedia.org/wiki/2019%E5%B9%B4%E4%B8%AD%E5%A4%AE%E5%B9%BF%E6%92%AD%E7%94%B5%E8%A7%86%E6%80%BB%E5%8F%B0%E6%98%A5%E8%8A%82%E8%81%94%E6%AC%A2%E6%99%9A%E4%BC%9A?oldformat=true")
except HTTPError as e:
    print("not found")
bsObj = BeautifulSoup(html,"html.parser")
tables = bsObj.findAll("table",{"class":"wikitable"})
if tables is None:
    print("no table");
    exit(1)
i = 1
for table in tables:
    fileName = "table%s.csv" % i
    rows = table.findAll("tr")
    csvFile = open(fileName,'wt',newline='',encoding='utf-8')
    writer = csv.writer(csvFile)
    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td','th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)
    finally:
        csvFile.close()
    i += 1