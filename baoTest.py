# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 16:04
# @Author  : zhouzz
# @FileName: baoTest.py
from functionTest import hello, add, Dome1

if __name__=="__main__":
	print hello
	print add(2,3)
	#print Dome1.add(2,5) TypeError: unbound method add() must be called
	print Dome1.f1()
	demo=Dome1()
	print demo.add(3,3)
