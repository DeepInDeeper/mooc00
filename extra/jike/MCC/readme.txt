Attention：
	1.ini文件用记事本打开进行更改保存，会出现"ConfigParser.MissingSectionHeaderError: File contains no section headers."()
	原因：
	 Window下用记事本打开配置文件并修改保存后，编码为UNICODE或UTF-8的文件的文件头会被相应的加上\xff\xfe（\xff\xfe）或\xef\xbb\xbf，然后再传递给ConfigParser解析的时候会出错，因此解析之前，先替换掉
	 解决方案：未解决。。。（现在是在用sublime TXT进行编辑文件）

	 2.ini文件需要填写自己的sina邮箱和密码。以及要sina邮箱打开POP3/SMTP

	 3.运行文件时 mcc.py

	 4.源自：极客学院 http://www.jikexueyuan.com/course/2120.html