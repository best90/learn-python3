#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 75:
            return 'B'
        elif self.__score >= 60:
            return 'C'
        else:
            return 'D'

mike = Student('Mike', 65)
print('mike.get_name is ', mike.get_name())
print('mike.get_score is ', mike.get_score())

mike.set_score(78)
print('mike.get_grade is ', mike.get_grade())

#内部的__name变量已经被Python解释器自动改成了_Student__name
print('Do not use mike._Student__name: ', mike._Student__name)