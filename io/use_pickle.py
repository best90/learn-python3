#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python提供了pickle模块来实现序列化

import pickle

d = dict(name='carlo', age=25, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)