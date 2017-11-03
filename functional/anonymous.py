#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(list(map(lambda x: x*x, [1,2,3,4,5])))

def f(x):
    return x * x
print(f(5))

l = lambda x: x * x
print(l(5))

def build(x, y):
    return lambda: x*x + y*y

b = build(1,2)
print(b())