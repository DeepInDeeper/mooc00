# -*- coding: cp936 -*-
import cookielib
import urllib2

#���ñ���cookie���ļ���ͬ��Ŀ¼�µ�cookie.txt
filename = 'cookie.txt'
#����һ��MozillaCookieJar����ʵ��������cookie��֮��д���ļ�
cookie = cookielib.MozillaCookieJar(filename)
#����urllib2���HTTPCookieProcessor����������cookie������
handler = urllib2.HTTPCookieProcessor(cookie)
#ͨ��handler������opener
opener = urllib2.build_opener(handler)
#����һ������ԭ��ͬurllib2��urlopen
response = opener.open("http://www.baidu.com")
#����cookie���ļ�
cookie.save(ignore_discard=True, ignore_expires=True)
