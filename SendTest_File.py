#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


my_sender='wangxinyuan_sign@aliyun.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user='715157026@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
file_path = ''
file_name = ''

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("2017-04-24", 'utf-8')
message['To'] = Header("适闲", 'utf-8')
subject = '每日签到文件-04-25-2017'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('今天的签到情况', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('/2017-04-24.zip', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="2017-04-24.zip"'
message.attach(att1)

# # 构造附件2，传送当前目录下的 runoob.txt 文件
# att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
# message.attach(att2)

try:
    server = smtplib.SMTP("smtp.aliyun.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, "wsx19961021")

    server.sendmail(my_sender, my_user, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
