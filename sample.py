#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import HTTPError
try:
  html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
except HTTPError as e:
  print("not found")
bsObj = BeautifulSoup(html,"html.parser")
table = bsObj.findAll("table",{"class":"wikitable"})[0]
if table is None:
  print("no table");
  exit(1)
rows = table.findAll("tr")
csvFile = open("editors.csv",'wt',newline='',encoding='utf-8-sing')
writer = csv.writer(csvFile)
try:
  for row in rows:
    csvRow = []
    for cell in row.findAll(['td','th']):
      csvRow.append(cell.get_text())
    writer.writerow(csvRow)
finally:
  csvFile.close()