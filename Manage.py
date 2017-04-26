import os
import SendTest_File
import re

#不知为什么，有什么会出现wlan0消失的情况
os.system('sudo ifconfig wlan0 up')


#查询wifi连接状态
k = os.popen("sudo wpa_cli status")
k = k.read()
wifi_name = re.findall('ssid=(.*?)\n',k,re.S)
if wifi_name:
	wifi_name = wifi_name[1]
	print(wifi_name)
else:
	print('wifi未连接！')

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


