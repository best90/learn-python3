#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import chardet

data = '离离原上草，一岁一枯荣'.encode('gbk')
result = chardet.detect(data)
print(result)