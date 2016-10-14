#!/usr/bin/env python
# encoding: utf-8
'''
lambda.py
lambda 的各种用法
python 2.7.x
'''

# 自增函数
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(0)
# 0 + 1
print f(1)
# 0 + 2
print f(2)

# 对数组内的tuple的第二个字段排序
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print pairs

# 对数组内的dict的age字段排序
arr = [
    {'name': 'asd', 'age': 4},
    {'name': 'asd', 'age': 1},
    {'name': 'asd', 'age': 3},
    {'name': 'asd', 'age': 2}
]
arr.sort(key=lambda people: people['age'])
print arr
