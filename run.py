#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :   run.py
@Time    :   2020/05/20 10:54:33
@Author  :   Zhang.Jia 
@Version :   1.0
@Contact :   947612227@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   文件创建完成
'''

from common.rang import path_to
from common.logger import Logger
import unittest
import HTMLTestRunner
import os
import sys
sys.path.append(os.getcwd())


def createTests():
    suite = unittest.TestSuite()
    testpath = path_to("casepath")
    testdir = unittest.defaultTestLoader.discover(
        testpath, pattern='test_*.py')

    for TestSuite in testdir:
        for testcase in TestSuite:
            suite.addTest(testcase)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # 定义报告存放的路径，支持相对路径
    file_path = path_to("reportpath")
    file_result = open(file_path, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=file_result, title=u"测试报告", tester=u"张佳",description=u"七只鸟创建客户测试报告",retry=1)
    runner.run(createTests())
    file_result.close()

    