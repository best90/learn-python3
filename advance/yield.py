#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def each_ascii(s):
    for ch in s:
        yield ord(ch)
    return '%s chars' % len(s)

def yield_from(s):
    r = yield from each_ascii(s)
    print (r)

def main():
    for x in each_ascii('abc'):
        print (x)
    it = each_ascii('xyz')
    try:
        while True:
            print (next(it))
    except StopIteration as s:
        print (s.value)

    for ch in yield_from('hello'):
        pass

main()