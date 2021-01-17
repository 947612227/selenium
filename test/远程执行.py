#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :   远程执行.py
@Time    :   2020/07/15 10:32:17
@Author  :   Zhang.Jia 
@Version :   1.0
@Contact :   947612227@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   文件创建完成
'''


from selenium import webdriver
import selenium.webdriver.remote.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor="http://127.0.0.1:4444/wd/hub",desired_capabilities=DesiredCapabilities.CHROME)

# driver = webdriver.Chrome()

url = "http://www.baidu.com"
driver.get(url)
driver.maximize_window()
driver.quit()


# java -jar selenium-server-standalone-2.40.0.jar -role node -hub http://localhost:4444/wd/hub -browser “browserName=chrome,maxinstance=1,platform=MAC” -Dwebdriver.chrome.driver=/usr/local/bin/chromedriver

