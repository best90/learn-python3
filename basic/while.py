#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 计算1+2+3+...+100:
sum = 0
n = 1
while n <= 100:
    sum += n
    n += 1
print (sum)

sum = 0
print ('求第一个数到最后一个数相加的和')
n = int(input('请输入第一个数: '))
m = int(input('请输入最后一个数:'))
while n <= m:
    sum += n
    n += 1
print (sum)

count = 1
n = 1
while n <= 100:
    count *= n
    n += 1
print (count)