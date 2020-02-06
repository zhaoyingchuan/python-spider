#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import HTTPError
try:
    html = urlopen("https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States")
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