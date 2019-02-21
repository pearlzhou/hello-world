# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 15:26
# @Author  : zhouzz
# @FileName: functionTest.py

hello="hello world"
def add(a,b):
	return  a+b

class Dome1(object):
	def __init__(self):
		pass

	def add(self, a,b):
		return a+b

	@staticmethod
	def f1():
		print "static method."
	def teardown(self):
		print "end!"

if __name__=="__main__":
	print hello
	print add(2,3)
	#print Dome1.add(2,5) TypeError: unbound method add() must be called
	print Dome1.f1()
	demo=Dome1()
	print demo.add(3,3)
