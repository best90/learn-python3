#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    __slots__ = ('name','age')
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

s = Student()
s.name = 'Tom'
s.age = 18

print(s.get_name())
print(s.get_age())
print(getattr(s, 'score', 90))

s.score = 90
print(s.score)