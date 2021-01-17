#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :   db_class.py
@Time    :   2020/05/25 23:04:35
@Author  :   Zhang.Jia 
@Version :   1.0
@Contact :   947612227@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   文件创建完成
'''


import os
import time
import pymysql

HOST = 'localhost'
PORT = 3306
USER = 'root'
PASS = 'zhangjia'
DBNAME = 'selenium'
CHARSET = 'utf8'
# TABLENAME = 'www'

class databaseClass:
    """测试环境数据库连接"""

    def dbinit():
        global db
        try:
            db = pymysql.connect(host=HOST, port=PORT, user=USER,
                        password=PASS, database=DBNAME, charset=CHARSET)
        except Exception as e:
            # print(1)
            print(e)
            # print(2)
        else:
            return db


# if __name__ == "__main__":
#     dbs = databaseClass
#     dbs.dbinit()
