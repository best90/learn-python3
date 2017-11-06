#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('type(123) = ', type(123))
print('type(\'123\') = ', type('123'))
print('type(None) = ', type(None))
print('type(abs) =', type(abs))
print('type(True) = ', type(True))
print('type([1,2,3,4]) = ', type([1,2,3,4]))

import types

print('type(\'abc\') == str?', type('abc') == str)