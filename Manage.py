import os
os.chdir('/')
os.system('sudo mv 2017-04-22 ~/SignInfo')
os.chdir('/home/pi/SignInfo')
os.system('sudo zip -r 2017-04-22.zip 2017-04-22')



