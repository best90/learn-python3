#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

# 查看当前目录的绝对路径
pwd = os.path.abspath('.')
print('     Size      Last Modified Name')
print('--------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d     %s      %s%s' % (fsize,mtime,f,flag))


file = os.path.join(pwd,'test.txt')
print(file)

path = os.path.split(file)
print(path)

os.mkdir(os.path.join(pwd,'test'))
os.rmdir(os.path.join(pwd,'test'))