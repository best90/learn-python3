#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def run_twice(self):
        self.run()
        self.run()

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
b = Dog()
c = Cat()
d = object()

print('a is Animal?', isinstance(a, Animal))
print('b is Animal?', isinstance(b, Animal))
print('c is Animal?', isinstance(c, Animal))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)
b.run_twice()

print(d)