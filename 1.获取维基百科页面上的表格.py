#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import HTTPError
try:
    html = urlopen("https://zh.wikisource.org/wiki/%E8%84%82%E7%A1%AF%E9%BD%8B%E9%87%8D%E8%A9%95%E7%9F%B3%E9%A0%AD%E8%A8%98/%E7%AC%AC%E5%8D%81%E4%B8%89%E5%9B%9E")
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
    csvFile = open(fileName,'wt',newline='',encoding='utf-8-sig')
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