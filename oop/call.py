#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name
	
	#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
	def __call__(self):
		print('My name is %s!' % self.name)

s = Student('Michael')
s()