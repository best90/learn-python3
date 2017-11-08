#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fn(self, name='world'):
    print('Hello, %s' % name)

#type()函数既可以返回一个对象的类型，又可以创建出新的类型
Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
print('call h.hello():')
h.hello()

print('type(Hello) =', type(Hello))
print('type(h) =', type(h))