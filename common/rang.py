#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :   rang.py
@Time    :   2020/05/22 16:40:53
@Author  :   Zhang.Jia 
@Version :   1.0
@Contact :   947612227@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   路径管理
'''

import os
import time
import random

rootpath = os.path.dirname(os.path.abspath('.')) + "/"
print(rootpath)
days = time.strftime("%Y-%m-%d",time.localtime())
datetime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
dates = time.strftime("%Y-%m-%d_%H", time.localtime())

def path_to(typename):
    """
    生成路径--参数说明
    logpath:日志
    casepath:测试用例
    image:截图
    """
    if typename == "logpath":
        path = rootpath + "selenium/log/log_" + days + ".log"
        # print(path)
        return path

    elif typename == "casepath":
        casepath = rootpath + "selenium/testcase/"
        return casepath

    elif typename == "image":
        image = rootpath + "selenium/screenshot/scr_" + datetime + ".png"
        return image
    elif typename == "reportpath":
        reportpath = rootpath + "selenium/htmlreport/" + dates + ".html"
        # reportpath = rootpath + "selenium/htmlreport/demo" + ".html"
        return reportpath
    elif typename == "phone":
            phonenum =  "137" + ''.join(str(random.choice(range(8))) for _ in range(8))
            print(phonenum)
            return phonenum

    else:
        print("参数不正确")

if __name__ == "__main__":

    path_to("phone")