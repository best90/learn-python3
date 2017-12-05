#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
time.sleep(5)

while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s: %s.' % addr)
    reply = 'Hello, %s' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)