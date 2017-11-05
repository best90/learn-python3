#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def get_score(self):
		print('%s: %s' % (self.name, self.score))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 75:
			return 'B'
		elif self.score >= 60:
			return 'C'
		else:
			return 'D'

john = Student('John', 90)
lily = Student('Lily', 99)
peter = Student('Peter', 69)
john.get_score()
print('His grade: %s' % (john.get_grade()))
lily.get_score()
print('Her grade: %s' % lily.get_grade())
peter.get_score
print('Grade of Peter: ', peter.get_grade())		