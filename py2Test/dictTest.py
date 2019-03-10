# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 下午4:33
# @Author  : zhouzz
# @FileName: dictTest.py

a = ["a", "b", "a", "c", "a", "c", "b", "d", "e", "c", "a", "c"]
duixiang = set(a)
print duixiang

d={}
for i in duixiang:
	d[i] = a.count(i)
print d
print d.items()
a1 = sorted(d.items(), key=lambda x: x[1], reverse=False)
print a1