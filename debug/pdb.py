#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#pdb.set_trace()暂停并进入pdb调试环境，
# 可以用命令p查看变量，或者用命令c继续运行

import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)