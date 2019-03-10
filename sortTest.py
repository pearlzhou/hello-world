# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 下午4:43
# @Author  : zhouzz
# @FileName: sortTest.py
"""sort仅针对于list对象排序，无返回值, 会改变原来队列顺序\
sorted是一个单独函数，可以对可迭代（iteration）对象排序，不局限于list，它不改变原生数据，重新生成一个新的队列"""

# a = [-9, 2, 3, -4, 5, 6, 6, 1]

# # 按从小到大排序
# a.sort()
# print(a)  # 结果：[-9, -4, 1, 2, 3, 5, 6, 6]
#
# # 按从大到小排序
# a.sort(reverse=True)
# print(a)  # 结果：[6, 6, 5, 3, 2, 1, -4, -9]

# def f(x):
# 	return abs(x)
# a.sort(key=f)
# print a


# # 1、list对象是字符串
# b = ["hello", "helloworld", "he", "hao", "good"]
# # 按list里面单词长度倒叙
# b.sort(key=lambda x: len(x), reverse=True)
# print(b)   # 结果：['helloworld', 'hello', 'good', 'hao', 'he']
#
# # 2、.list对象是元组
# c = [("a", 9), ("b", 2), ("d", 5)]
#
# # 按元组里面第二个数排序
# c.sort(key=lambda x: x[1])
# print(c)  # 结果：[('b', 2), ('d', 5), ('a', 9)]
#
# # 3、list对象是字典
# d = [{"a": 9}, {"b": 29}, {"d":5}]
# # for i in d:
# # 	print list(i.values())[0]
#
# # d.sort(key=lambda x: x.values())
# d.sort(key=lambda x: list(x.values())[0])
# print(d)  # 结果：[{'b': 2}, {'d': 5}, {'a': 9}]

"""iterable 可迭代对象，如：str、list、tuple、dict都是可迭代对象（这里就不局限于list了）

key 用列表元素的某个属性或函数进行作为关键字（此函数只能有一个参数）

reverse 排序规则. reverse = True 降序或者 reverse = False 升序，默认升序
return 有返回值值，返回新的队列"""

a = [-9, 2, 3, -4, 5, 6, 6, 1]

# 按从小到大排序
b = sorted(a)
print(a)   # a不会变
print(b)   # b是新的队列 [-9, -4, 1, 2, 3, 5, 6, 6]

# 按从大到小排序
c = sorted(a, reverse=True)
print(c)  # 结果：[6, 6, 5, 3, 2, 1, -4, -9]

# 字符串也可以排序

s = "hello world!"
d = sorted(s)
print(d)  # 结果：[' ', '!', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']

# 元组也可以排序
t = (-9, 2, 7, 3, 5)
n = sorted(t)
print(n)  # 结果：[-9, 2, 3, 5, 7]

# dict按value排序
f = {"a": 9, "b": 2, "d": 5}
g = sorted(f.items(), key=lambda x: x[1])
print(g)  # 结果：[('b', 2), ('d', 5), ('a', 9)]