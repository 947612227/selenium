#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :   basePage.py
@Time    :   2020/05/20 13:35:13
@Author  :   Zhang.Jia 
@Version :   1.0
@Contact :   947612227@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   文件创建完成
'''
from time import sleep
from common.logger import Logger
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains    #鼠标悬停
import selenium.webdriver.remote.webdriver
from selenium import webdriver
import sys
import os
sys.path.append(os.getcwd())


pa = name = os.path.basename(__file__)
logger = Logger(logger=pa).getlog()
logger.info("开始执行测试用例")


class base(object):
    """
    基类调用方法
    """

    def __init__(self):
        """初始化全局变量"""
        self.driver = driver
        self.url = url
        print(pa)
        # self.log = log
        # self.rg = rg

    def getFilePath():
        return sys.argv[0]

    def driverInit(url, drivertype=None, way=None, cookies=None):
        """初始化驱动"""
        logger.info("准备初始化浏览器驱动")
        if url == None:
            logger.warning(str(sys.argv[0]) + " 文件缺少URL参数")

        else:
            if drivertype == None:
                # driver = webdriver.Chrome()
                driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor="http://127.0.0.1:4444/wd/hub",desired_capabilities=DesiredCapabilities.CHROME)
                driver.get(url)
                # driver.add_cookie(cookie_dict=cookies)
                # driver.refresh()
                driver.maximize_window()
                logger.info("Chrome浏览器初始化完成-->" + url + "-->" + driver.title)
                return driver
            elif drivertype == 1:
                driver = webdriver.Firefox()
                driver.get(url)
                driver.maximize_window()
                logger.info("Firefox浏览器初始化完成-->" + url + "-->" + driver.title)
                return driver
            else:
                logger.warning("缺少参数或暂不支持该浏览器")

    def waits(driver,  type, name, descript=None, i=None):
        """
        显示等待
        WebDriverWait
        diver:驱动
        i:每i秒轮查一次
        type:id,name,css,xpath
        descript:定位元素描述
        """
        if descript == None:
            descript = "未填写描述"
        if i == None:
            i = 5

        if type == 'id':
            try:
                wait = WebDriverWait(driver, i).until(
                    lambda x: x.find_element_by_id(name))

            except Exception as e:
                logger.error(str(e))
            else:
                logger.info("发现元素->" + descript + ":" + name)
                print("发现元素->" + descript + ":" + name)
                obj = driver.find_element_by_id(name)
                return obj

        elif type == 'name':
            try:
                wait = WebDriverWait(driver, i).until(
                    lambda x: x.find_element_by_name(name))
            except Exception as e:
                logger.error(str(e))
            else:
                logger.info("发现元素->" + descript + ":" + name)
                print("发现元素->" + descript + ":" + name)
                obj = driver.find_element_by_name(name)
                return obj

        elif type == 'css':
            try:
                wait = WebDriverWait(driver, i).until(
                    lambda x: x.find_element_by_css(name))
            except Exception as e:
                logger.error(str(e))
            else:
                logger.info("发现元素->" + descript + ":" + name)
                print("发现元素->" + descript + ":" + name)
                obj = driver.find_element_by_css(name)
                return obj

        elif type == 'xpath':
            try:
                wait = WebDriverWait(driver, i).until(
                    lambda x: x.find_element_by_xpath(name))
            except Exception as e:
                logger.error(str(e))
            else:
                logger.info("发现元素->" + descript + ":" + name)
                print("发现元素->" + descript + ":" + name)
                obj = driver.find_element_by_xpath(name)
                return obj

        elif type == 'xpaths':
            try:
                wait = WebDriverWait(driver, i).until(
                    lambda x: x.find_elements_by_xpath(name))
            except Exception as e:
                logger.error(str(e))
            else:
                logger.info("发现元素->" + descript + ":" + name)
                print("发现元素->" + descript + ":" + name)
                obj = driver.find_elements_by_xpath(name)[1].click
                return obj

        elif type == 'select':
            try:
                wait = WebDriverWait(driver, i).until(
                    lambda x: x.find_element_by_css_selector(name))
            except Exception as e:
                logger.error(str(e))
            else:
                logger.info("发现元素->" + descript + ":" + name)
                print("发现元素->" + descript + ":" + name)
                obj = driver.find_element_by_css_selector(name)
                return obj

        elif type == 'classname':
            try:
                wait = WebDriverWait(driver, i).until(
                    lambda x: x.find_element_by_class_name(name))
            except TimeoutException as e:
                logger.error(str(e))
            else:
                logger.info("发现元素->" + descript + ":" + name)
                print("发现元素->" + descript + ":" + name)
                obj = driver.find_element_by_class_name(name)
                return obj

        elif type == 'text':
            try:
                wait = WebDriverWait(driver, i).until(
                    lambda x: x.find_element_by_link_text(name))
            except Exception as e:
                logger.error(str(e))
            else:
                logger.info("发现元素->" + descript + ":" + name)
                print("发现元素->" + descript + ":" + name)
                obj = driver.find_element_by_link_text(name)
                return obj

        else:
            logger.error( "文件参数错误")
            print( "文件参数错误")

    def swich_handle(driver):
        handles = driver.window_handles  # 获取窗口句柄
        logger.info("获取窗口句柄完成" + str(handles))
        print("获取窗口句柄完成" + str(handles))
        driver.switch_to_window(handles[-1])  # 跳转窗口
        logger.info("跳转窗口完成")
        print("跳转窗口完成")

    def sciptexc(driver, js):
        driver.execute_script(js)
        sleep(0.5)
        logger.info("调用js_exec完成：" + js)

    # 鼠标悬停
    def hover(driver,ele):
        actions = ActionChains(driver)
        actions.move_to_element(ele)


"""
    if __name__ == "__main__":
        url = "https://www.baidu.com"
        driver = driverInit(url)
        keyword = waits(driver, "id", "kw")
        keyword.send_keys("12306")
        search_btn = waits(driver, "id", "su")
        search_btn.click()
        # driver.close()
        # 相同的元素选择第一个
        temp = waits(driver, "xpath",
                     "//div[@class='result-op c-container'][1]/h3/a[1]")
        temp.click()
        swich_handle(driver)
        logger.info(driver.title)
        # print(driver.title)

        # 定位出发城市，输入框
        start = waits(driver, "id", "fromStationText")
        # 需要先点击输入框
        start.click()  # 点击出发城市
        # 输入北京
        start.send_keys("北京")

        # 定位弹出来的联想词框
        select_city = waits(driver, "xpath", "//*[@class='popcitylist']/li[1]")

        # 定位要选择的城市
        start_id = driver.find_element_by_id("citem_2")
        # 鼠标移动到要选择的城市上，点击start_id
        ActionChains(driver).move_to_element(
            start_id).click(start_id).perform()

        end = waits(driver, "id", "toStationText")
        end.click()
        # end.send_keys("成都")
        # end_id = driver.find_element_by_id("citem_2")
        select_end = waits(driver, "xpath", "//*[@class='popcitylist']/li[7]")
        ActionChains(driver).move_to_element(
            select_end).click(select_end).perform()

        # 选择出发日期
        # send_time = waits(driver, "id", "train_date")
        # send_time.click()
        # js = 'document.getElementById("train_date").removeAttribute("readonly");'
        # sciptexc(driver, js)  # 去掉只读属性
        # send_time.send_keys("2020-05-30")
        # send_time.send_keys(Keys.ENTER)
        # 点击查询按钮
        time_str = waits(driver, "id", "search_one").click()

        swich_handle(driver)
        waits(driver, "id", "sear-result")
        sleep(3)
        src_path = "/Users/admin/Desktop/code/Python/selenium/screenshot/res.png"
        driver.get_screenshot_as_file(src_path)
        # 结果截图保存
        sleep(4)
        driver.quit()
"""

def getFilePath():
    return sys.argv[0]

# def driverInit(url, drivertype=None, way=None,cookies=None):
#     """初始化驱动"""
#     logger.info("准备初始化浏览器驱动")
#     if url == None:
#         logger.warning(str(sys.argv[0]) + " 文件缺少URL参数")

#     else:
#         if drivertype == None:
#             driver = webdriver.Chrome()

#             driver.get(url)
#             # driver.add_cookie(cookie_dict=cookies)
#             # driver.refresh()
#             driver.maximize_window()
#             logger.info("Chrome浏览器初始化完成-->"+ url + "-->" + driver.title)
#             return driver
#         elif drivertype == 1:
#             driver = webdriver.Firefox()
#             driver.get(url)
#             driver.maximize_window()
#             logger.info("Firefox浏览器初始化完成-->"+ url + "-->" + driver.title)
#             return driver

#         else:
#             logger.warning("缺少参数或暂不支持该浏览器")
