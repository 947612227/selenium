#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :   test_12306.py
@Time    :   2020/05/22 17:18:20
@Author  :   Zhang.Jia
@Version :   1.0
@Contact :   947612227@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   文件创建完成
'''
import unittest
import pymysql
from common.basePage import base
from common.logger import Logger
from bs4 import BeautifulSoup
from time import sleep
import sys
import os
sys.path.append(os.getcwd())

HOST = 'localhost'
PORT = 3306
USER = 'root'
PASS = 'zhangjia'
DBNAME = 'selenium'
CHARSET = 'utf8'
# global db
logger = Logger(logger="test_by12306.py").getlog()
logger.info("初始化日志模块完成")

class TestCase(unittest.TestCase):
    """测试用例模块"""

    def setUp(self):
        """初始化unittest前置条件"""
        pass



    def tearDown(self):
        """初始化unittest后置条件"""
        logger.info("准备退出chromedriver")
        

    # def dbinit(self):
    def insert_data_sql(self, a, b):
        """将爬取到的数据插入到数据库中"""
        if a != None and b != None:
            try:
                db = pymysql.connect(host=HOST, port=PORT, user=USER,
                                     password=PASS, database=DBNAME, charset=CHARSET)
            except Exception as e:
                print(e)
            else:
                cursor = db.cursor()
                # return cursor

                sql = "insert into search_baidu (name,url) values ('" + pymysql.escape_string(
                    a) + "'," + "'" + pymysql.escape_string(b) + "'" + ");"

                try:
                    cursor.execute(sql)
                    logger.info(sql)
                except Exception as e:
                    logger.info('异常：' + str(e))
                else:
                    db.commit()
                    logger.info('数据提交完成：')
                finally:
                    # 
                    sleep(1)
                    db.close()
                    # db.cursor()
        else:
            logger.info("表字段数据不能为空")

    def test_baidu(self):
        """
        第一个测试用例
        """
        n = 0
        bdcookie = {
            "value": "31658_1421_31326_21107_31111_31254_31594_31464_30824_26350_22158", "name": "H_PS_PSSID"}
        for j in range(0,10):
            n+=1
            url = "https://www.baidu.com/s?ie=UTF-8&wd=110&pn="+str(j*10 + 10)
            # driver = base.driverInit(url, cookies=bdcookie)
            driver = base.driverInit(url, cookies=bdcookie)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            for i in soup.find_all(class_="t"):
                a = str(i.a.string)
                b = str(i.a['href'])
                logger.info(str(n) + "-->"+ a)
                logger.info(str(n) +"-->"+ b)
                self.insert_data_sql(a, b)
            driver.quit()    
