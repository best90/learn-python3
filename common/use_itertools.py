#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

#count()会创建一个无限的迭代器
natuals = itertools.count(1)
for n in  natuals:
    print(n)
    if n >= 100:
        break

# cycle()会把传入的一个序列无限重复
cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A',5)
for n in ns:
    print(n)

#takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x <=10, natuals)
print(list(ns))

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC','XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AaaBbbcCcaAAa', lambda c:c.upper()):
    print(key, list(group))

