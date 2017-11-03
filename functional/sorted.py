#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

print(sorted([3,45,4,8,1]))

L = ['Boy','Girl','man','Woman']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75),('Adam', 92),('Bart',66),('Lisa', 81)]
print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))