#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Demo(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = Demo()
print('hasattr(obj,\'x\') =', hasattr(obj, 'x'))
print('hasattr(obj,\'y\') =', hasattr(obj, 'y'))

setattr(obj,'y', 10)
print('hasattr(obj,\'x\') =', hasattr(obj, 'x'))
print('hasattr(obj,\'y\') =', hasattr(obj, 'y'))

y = getattr(obj,'y')
print(y)

z = getattr(obj, 'z', 11)
print(z)

f = getattr(obj,'power', 11)
print(f)
print(f())