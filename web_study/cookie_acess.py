# -*- coding: cp936 -*-
import cookielib
import urllib2

#����MozillaCookieJarʵ������
cookie = cookielib.MozillaCookieJar()
#���ļ��ж�ȡcookie���ݵ�����
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#���������request
req = urllib2.Request("http://www.baidu.com")
#����urllib2��build_opener��������һ��opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
