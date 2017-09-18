#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power(x):
    return x * x

print (power(1))

def info(data):
    for name, age in data.items():
        print ('name: ',name,' age: ', age)
    print ()

data = {
    'Jack': 18,
    'Lily': 17,
    'Ben': 34
}

print (info(data))