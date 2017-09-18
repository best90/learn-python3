#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(n):
    if n == 1:
        return 1
    return  n * func(n-1)

print ('test func(1) =', func(1))
print ('test func(2) =', func(2))
print ('test func(3) =', func(3))