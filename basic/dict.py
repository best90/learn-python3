#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dict = {
    'name': 'carlo',
    'age': 25,
    'sex': 'male'
}

print ('name: ',dict['name'])
print ('age: ',dict['age'])
print ('sex: ',dict['sex'])

# get()获取字典相对应的value
print (dict.get('age'))