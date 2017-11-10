#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

# StringIO顾名思义就是在内存中读写str
f = StringIO()
f.write('hello, world')
f.write('! ')
f.write('C')
print(f.getvalue())

f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())