#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.xrspace.com')
soup = BeautifulSoup(response.text)
print(soup.title.text)
print(soup.body.text)

for x in soup.findAll("a"):
    print(x["href"])


soup = BeautifulSoup(requests.get("http://www.zhihu.com").text)
print(soup.find("input", {"name": "_xsrf"})['value'])
