#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple
#namedtuple是一个函数，它用来创建一个自定义的tuple对象
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print('Point:', p.x, p.y)


from collections import deque
# deque除了实现list的append()和pop()外，
# 还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


from collections import defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd = defaultdict(lambda :'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] = ', dd['key1'])
print('dd[\'key2\'] = ', dd['key2'])


from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
od = OrderedDict(d)
print(od)


from collections import Counter
#Counter是一个简单的计数器
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)