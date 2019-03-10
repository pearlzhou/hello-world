# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 下午4:05
# @Author  : zhouzz
# @FileName: osTest.py
import os
a=os.system(r'python /Users/zhenzhuzhou/pearl/hello.py')
print a

f=os.popen(r'python /Users/zhenzhuzhou/pearl/hello.py', 'r') #用法同open
d=f.read()
print d
print type(d)
f.close()

