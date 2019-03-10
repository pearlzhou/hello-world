# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 下午7:53
# @Author  : zhouzz
# @FileName: yamlTest1.py


import os
from ruamel import yaml
# 将字典写入到yaml
desired_caps = {
                'platformName': 'Android',
                'platformVersion': '7.0',
                'deviceName': 'A5RNW18316011440',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Uiautomator2',
                'unicodeKeyboard': [True,"hh"],
                'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
                }

curpath = os.path.dirname(os.path.realpath(__file__))
print curpath
yamlpath = os.path.join(curpath, "caps.yaml")

# 写入到yaml文件
with open(yamlpath, "w") as f:
    yaml.dump(desired_caps, f,Dumper=yaml.RoundTripDumper)

a = open(yamlpath, "r")
print(yaml.load(a.read(),Loader=yaml.Loader))