#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :   test_szjw_system_manger.py
@Time    :   2020/08/03 11:23:08
@Author  :   Zhang.Jia 
@Version :   1.0
@Contact :   947612227@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   文件创建完成
'''



import sys
import os
sys.path.append(os.getcwd())
import unittest
import pymysql
from common.rang import path_to
from common.basePage import base
from common.logger import Logger
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

pa = name=os.path.basename(__file__)
logger = Logger(logger=pa).getlog()
# logger.info("初始化日志模块完成")

class TestCase(unittest.TestCase):
    """测试用例模块"""

    def setUp(self):
        """初始化unittest前置条件"""
        logger.info("初始化日志模块完成")
        url = "http://szjw-bss-web.m1.yunniao.cn/"
        self.driver = base.driverInit(url)


    def tearDown(self):
        """初始化unittest后置条件"""
        self.driver.quit()
        logger.info("已退出驱动程序")

    def login(self,uName,uPswd):
        """登录"""
        print("准备登陆")
        logger.info("准备登陆")
        username = base.waits(self.driver,"name","username","用户名输入框")
        username.clear()
        username.send_keys(uName)
        print("输入:",uName)
        password = base.waits(self.driver,"name","password","密码输入框")
        password.clear()
        password.send_keys(uPswd)
        print("输入:",uPswd)
        login_btn = base.waits(self.driver,"select","#app > div > form > div.wrapper > button","登录按钮")
        sleep(1)
        login_btn.click()
        print("点击登录按钮")
    
        # self.driver.refresh()
        logger.info("登录完成")



    def test_login_case1(self):
        """测试正常登录"""
        uName = '13488883948'
        uPass = '18888888888'
        self.login(uName,uPass)
        pUser = base.waits(self.driver,"xpath",'//*[@id="app"]/div/div[2]/section/div/div/div/div/div/div[1]/div/span',"判断登录是否成功")
        name = pUser.get_attribute('textContent')
        print(name)
        assert (name == "账号详情")


    def test_login_case2(self):
        """错误的账号密码"""
        uName = 'zhangjia'
        uPass = '1348883948'
        self.login(uName,uPass)
        tips = base.waits(self.driver,"xpath",'/html/body/div[2]/p','捕捉登录失败提示').get_attribute("textContent")
        print(tips)
        assert (tips == "用户名输入错误")

    def test_z_create_line(self):
        """新建司机"""
        #先登录
        uName = '13488883948'
        uPass = '18888888888'
        self.login(uName,uPass)
        #运力中心菜单
        menuYlzx = base.waits(self.driver,"xpath",'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/div/span[2]','运力中心菜单').click()

        #司机线索菜单    
        menuSjxs = base.waits(self.driver,'text','司机线索','司机线索菜单').click()

        sleep(2)
        #创建线索按钮  --- 很不稳定
        createLineBtn = base.waits(self.driver,'select','#app > div > div.main-container.hasTagsView > section > div > div.TableHeader > div.TableHeader_button > button:nth-child(1)','创建线索按钮').click()
        # createLineBtn.click()

        """人工线索录入"""
        #姓名
        name = base.waits(self.driver,'xpath','//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/form/div[1]/div/div/div/input','姓名输入框').send_keys('张佳')

        #电话
        phonenum = path_to('phone')
        phone = base.waits(self.driver,'xpath','//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/form/div[2]/div/div/div/input','电话输入框').send_keys(phonenum)

        #微信
        weChatNo = base.waits(self.driver,'xpath','//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/form/div[3]/div/div/div/input','微信输入框').send_keys("zhangjia_test")

        #工作城市--二次选择input --直接输入城市后--需要啊hover到选择项才行
        workCitySelect = base.waits(self.driver,'xpath','//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/form/div[4]/div/div/div/div[1]/input','工作城市选择')
        workCitySelect.send_keys('南充市')

        #工作城市弹出层
        # js1 = 'document.getElementsByClassName("el-select-dropdown__item")[1].click;'
        # self.driver.execute_script(js1)
        sleep(1)
        selectCity = base.waits(self.driver,'xpath','//*[text()="南充市"]','选择城市-南充市')
        ActionChains(self.driver).move_to_element(selectCity).perform()
        js1 = "document.getElementsByClassName('hover')[0].click();"
        self.driver.execute_script(js1)

        #车型
        
        carType = base.waits(self.driver,'xpath','//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/form/div[5]/div/div/div/div[1]/input','车型选择').send_keys("4.2米厢货(有证)")
        sleep(1)

        #执行js
        selectCar = base.waits(self.driver,'xpath','//*[text()="4.2米厢货(有证)"]','选择车型4.2米厢货(有证)')
        ActionChains(self.driver).move_to_element(selectCar).perform()
        js2 = "document.getElementsByClassName('hover')[1].click();"
        self.driver.execute_script(js2)

        #来源渠道
        source = base.waits(self.driver,'xpath','//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/form/div[6]/div/div/div/div/input','来源渠道选择').send_keys("58同城")

        #执行js
        selectSource = base.waits(self.driver,'xpath','//*[text()="58同城"]','选择来源为-58同城')
        ActionChains(self.driver).move_to_element(selectSource).perform()
        js3 = "document.getElementsByClassName('hover')[2].click();"
        self.driver.execute_script(js3)

        #业务线
        workline = base.waits(self.driver,'xpath','//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/form/div[7]/div/div/div/div[1]/input','业务线选择')
        js5 = 'arguments[0].removeAttribute(\"readonly\");'
        self.driver.execute_script(js5, workline)
        workline.click()


        selectworkline = base.waits(self.driver,'xpath','//*[text()="专车"]','选择来源为-58同城')
        ActionChains(self.driver).move_to_element(selectworkline).perform()
        # js4 = "document.getElementsByClassName('hover')[3].click();"
        # self.driver.execute_script(js4)
        selectworkline.click()


        #点击保存按钮
        saveBtn = base.waits(self.driver,'xpath','//*[@name="driverclue_save_btn"]','保存按钮').click()
        # sleep(10)


        #接下来验证是否添加成功，返回线索列表查询  phonenum
        pAddLine = base.waits(self.driver,"xpath",'//*[text()="操作成功"]',"判断添加线索是否成功")
        pAddLineRes = pAddLine.get_attribute('textContent')
        assert (pAddLineRes == "操作成功")




