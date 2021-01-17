#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   seleniumtest.py
@Time    :   2020/12/09 17:04:04
@Author  :   Zhang Jia 
@Version :   1.0
@Contact :   zhang.jia@yunniao.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
'''

# here put the import lib
from selenium import webdriver
import requests
import json
import time
now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# requests.packages.urllib3.disable_warnings()


class login:
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_windows()
        print(0)

    def get_p(self):
        self.driver.get("http://www.baidu.com")
        print(1)


a = login().get_p()
