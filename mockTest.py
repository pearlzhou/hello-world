# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 下午9:48
# @Author  : zhouzz
# @FileName: mockTest.py

import mock
import unittest
import mockbase


class Test_zhifu_statues(unittest.TestCase):
	'''单元测试用例'''
	def test_01(self):
		'''测试支付成功场景'''
		# mock 一个支付成功的数据
		mockbase.zhifu = mock.Mock(return_value={"result": "success", "reason":"null"})
		# 根据支付结果测试页面跳转
		statues = mockbase.zhifu_statues()
		print(statues)
		self.assertEqual(statues, "支付成功")

	def test_02(self):
		'''测试支付失败场景'''
		# mock 一个支付成功的数据
		mockbase.zhifu = mock.Mock(return_value={"result": "fail", "reason": "余额不足"})
		# 根据支付结果测试页面跳转
		statues = mockbase.zhifu_statues()
		self.assertEqual(statues, "支付失败")

if __name__== "__main__":
	unittest.main()
