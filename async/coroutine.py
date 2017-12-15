#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#协程效率极高，因为子程序切换不是线程切换，程序自身控制。没有线程切换的开销
# 不需要多线程的锁机制
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)