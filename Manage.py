import os
import SendTest_File
import re


os.chdir('/')
file_name = '2017-04-13'

isExists = os.path.exists(file_name)


if isExists:
	os.chdir('/')
	command_mv_file = 'sudo mv ' + file_name + ' ~/SignInfo'
	os.system(command_mv_file)
	command_cd_host = '/home/pi/SignInfo'
	os.chdir(command_cd_host)
	command_zip_file = 'sudo zip -r ' + file_name + '.zip' + ' ' + file_name
	os.system(command_zip_file)
	the_file_path = command_cd_host + '/' + file_name + '.zip'
	the_file_name = file_name + '.zip'
	SendTest_File.send_email(the_file_path,the_file_name,file_name)	
	
else:
	print('文件已转移！')


