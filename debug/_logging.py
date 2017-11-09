#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#logging模块可以非常容易地记录错误信息

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)