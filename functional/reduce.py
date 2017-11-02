#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def add(x,y):
    return x+y

print(reduce(add, [1,3,5,7,9]))

def fn(x, y):
    return x*10 + y

print(reduce(fn, [1,3,5,7,9]))

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(reduce(fn, map(char2num, '13579')))

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))