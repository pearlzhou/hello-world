# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 下午8:05
# @Author  : zhouzz
# @FileName: funTest.py

import sys
"""在函数外部获取函数的名称，用.__name__获取"""
def zhenzhu():
	print "hello world!"
n = zhenzhu.__name__
print n

"""在函数内部获取当前函数的名称，用sys._getframe().f_code.co_name"""

def yo_yo():
	print "当前函数的名称为：%s" %sys._getframe().f_code.co_name


"""获取类和方法的名称，取名称self.__class__.__name__"""
"""在类里获取类方法跟在函数内获取函数名称一样，sys._getframe().f_code.co_name"""

class YoYo():
	def yoyo(self):
		print "当前类名称为：%s" % self.__class__.__name__
		print "当前类方法名称为：%s" %sys._getframe().f_code.co_name
if __name__ == '__main__':
	yo_yo()
	YoYo().yoyo()