import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}

url = r"https://pro.arcgis.com/en/pro-app/sdk/api-reference/#topic1.html"

response = requests.get(url, headers=headers).text

print(response)