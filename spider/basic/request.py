#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

url = 'http://www.baidu.com/'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print(response.info())
print(response.getcode())
print(response.read())