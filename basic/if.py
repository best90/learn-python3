#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#input() 返回的是字符串
#int() 将字符串转换为整数，才能进行数值比较
age = int(input('Input your age: '))

if age > 18 :
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')