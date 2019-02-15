# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 16:34
# @Author  : zhouzz
# @FileName: jenkintest.py

# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 16:31
# @Author  : zhouzz
# @FileName: p12test.py


from unittest import TestCase

#!/usr/bin/python
#-*- conding=utf-8 -*-
class test_aaa(TestCase):

	def setUp(self):
		print "setUp"


	#attr("priority3")
	def test_qqq(self):
		u'qqqq test'
		print "1111"

	#@attr("priority3")
	def test_fff(self):
		u'ffff test'
		print "2222"

	def tearDown(self):
		print "tearDwon"
