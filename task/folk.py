#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())

# Only works on Unix/Linux/Mac
# 子进程永远返回0，而父进程返回子进程的ID
# 子进程只需要调用getppid()就可以拿到父进程的ID
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))