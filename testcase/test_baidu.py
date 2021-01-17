#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   test_baidu.py
@Time    :   2020/12/16 17:37:01
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
from time import sleep

url = "http://news.baidu.com/"

driver = webdriver.Chrome()
driver.get(url)

sleep(2)
x = driver.find_element_by_xpath(
    '// *[@id="pane-news"]/div/ul/li[3]/strong/a[1]')

sleep(1)
x.click()
sleep(5)
driver.quit()
