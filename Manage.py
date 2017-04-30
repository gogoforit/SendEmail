import os
import SendTest_File
import re

#ap开启再关闭以后，会出现wlan0消失的情况，暂时只能这么处理了
os.system('sudo ifconfig wlan0 up')


#查询wifi连接状态
def query_wifi_status():
	k = os.popen("sudo wpa_cli status")
	k = k.read()
	wifi_name = re.findall('ssid=(.*?)\n',k,re.S)
	wifi_status = False
	if wifi_name:
		wifi_name = wifi_name[1]
		wifi_status = True
		print(wifi_name)
	else:
		print('wifi未连接！')
	return wifi_status	

#把所有没有发送的文件列出来
def list_all_files():
	last_list = []
	os.chdir('/')
	k = os.popen('ls -d 20*')	
	k = k.read()
	files_list = k.split('\n')
	for each in files_list:
		if each != '':
			#print(each)
			last_list.append(each)
	#print(k)
	print(last_list)
	return last_list

#压缩并把文件已邮件的形式发送出去
def compressFile_sendEmail(name):

	os.chdir('/')
	file_name = name

	isExists = os.path.exists(file_name)
	command_transfer = '/home/pi/SignInfo/' + file_name
	isTransfer = os.path.exists(command_transfer)

	if isExists and isTransfer == False:
		os.chdir('/')
		command_mv_file = 'sudo mv ' + file_name + ' home/pi/SignInfo'
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

if __name__ == '__main__':
	while True:
		status = query_wifi_status()
		if status == True:
			file_list = list_all_files()
			for each in file_list:
				compressFile_sendEmail(each)
		else:
			pass	



