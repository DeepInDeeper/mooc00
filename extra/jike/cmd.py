import os
import time

while True:
	file_open=open('conf.txt','r')
	content= file_open.read()
	os.system(content)
	time.sleep(5)