#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a demo module'

__author__ = 'demo'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('hello, world!')
	elif len(args) == 2:
		print('hello, %s!' % args[1])
	else:
		print('Too many arguments!')

if __name__ == '__main__':
	test()