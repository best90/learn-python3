#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def lazy_sum(*args):
    def sum():
        a = 0
        for n in args:
            a = a + n
        return a
    return sum

f = lazy_sum(1,2,3,4,5)
print(f)
print(f())

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print (f1())
print (f2())
print (f3())

def count():
    fs = []
    def f(n):
        def j():
            return n*n
        return j
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print (f1())
print (f2())
print (f3())