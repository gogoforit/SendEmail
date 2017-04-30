#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_email(file_path,file_name,the_time):
	my_sender='wangxinyuan_sign@aliyun.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
	my_user='715157026@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
	my_user2 = 'wangxinyuan_info@aliyun.com'
	#file_path = ''
	#file_name = ''
	title_name = '每日签到文件' + the_time 

	# 创建一个带附件的实例
	message = MIMEMultipart()
	message['From'] = Header("网信院签到", 'utf-8')
	message['To'] = Header("适闲", 'utf-8')
	subject = title_name
	message['Subject'] = Header(subject, 'utf-8')

	# 邮件正文内容
	message.attach(MIMEText('今天的签到情况,见附件', 'plain', 'utf-8'))

	# 构造附件1，传送当前目录下的 test.txt 文件
	att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
	att1["Content-Type"] = 'application/octet-stream'
	# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
	#构造发送的文件名字
	the_command = 'attachment; filename=' + '"'+ file_name +'"' + "'"
	print(the_command)
	att1["Content-Disposition"] = the_command
	#att1["Content-Disposition"] = 'attachment; filename="2017-04-05.zip"'
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
	    print("1邮件发送成功")
	    server.sendmail(my_sender, my_user2, message.as_string())
	    print("2邮件发送成功")

	except smtplib.SMTPException:
	    print("Error: 无法发送邮件")
