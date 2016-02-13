import win32api
import time

while True:
	file_open=open('message.txt','r')
	content=file_open.read().split('#')
	if content[0] != '0':
		win32api.MessageBox(0,content[1],content[2])
	time.sleep(5)