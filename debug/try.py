#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# except语句块不会被执行，但是finally如果有，则一定会被执行
try:
    print('try...')
    r = 10 / 0
    print('result: ', r)
except ZeroDivisionError as e:
    print('except: ', e)
finally:
    print('finally...')
print('END')