#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def my_func(x):
    if not isinstance(x, (int, float)):
        raise  TypeError('error type')
    if x >= 0:
        return x
    else:
        return -x

print (my_func(-1))
print (my_func(10))
print (my_func('100'))