#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

odd = list(filter(is_odd, [1,2,3,4,5,6,7,8,9]))
print(odd)

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['a','','b', None,'c','  '])))