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

