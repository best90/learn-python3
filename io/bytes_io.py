#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())