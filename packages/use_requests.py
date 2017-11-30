#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get('https://www.douban.com')
print(r.status_code)
print(r.text)
print(r.encoding)

r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r.text)