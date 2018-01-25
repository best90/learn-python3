#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import http.cookiejar
import urllib.request
import urllib.parse
import re
import gzip

def ungzip(data):
    try:
        print('正在解压...')
        data = gzip.decompress(data)
        print('解压完毕！')
    except:
        print('未经压缩，无需解压')
    return data

def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags=0)
    strlist = cer.findall(data)
    _xsrf = strlist[0] if len(strlist) else ''
    return _xsrf

def getOpener(head):
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key,value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}

url = 'http://www.zhihu.com/'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)
_xsrf = getXSRF(data.decode())

url += 'login'
id = 'username'
password = 'password'
postDict = {
    '_xsrf':_xsrf,
    'email': id,
    'password': password,
    'rememberme': 'y'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print(data.decode())