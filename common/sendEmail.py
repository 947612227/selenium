#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :   sendEmail.py
@Time    :   2020/07/09 17:14:48
@Author  :   Zhang.Jia 
@Version :   1.0
@Contact :   947612227@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   文件创建完成
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# 第三方 SMTP 服务
mail_host = 'smtp.263.net' #设置服务器
mail_user = 'zhangjia@yunniao.me'   #用户名
mail_pass = 'Pwd123' #口令 
 
 
sender = 'zhangjia@yunniao.me'
receivers = ['947612227@qq.com', 'zhangjia@yunniao.me']   # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
#邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
 
# 构造附件1，传送当前目录下的 test.txt 文件
file1 = "/Users/admin/Desktop/code/Python/selenium/htmlreport/2020-07-09_16.html"
att1 = MIMEText(open(file1, 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="测试报告.html"'
message.attach(att1)
 

 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 465)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")