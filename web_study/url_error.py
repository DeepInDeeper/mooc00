# -*- coding: cp936 -*-
#异常处理
import urllib2
# 网址错误
requset = urllib2.Request('http://www.xxxxx.com')
try:
    urllib2.urlopen(requset)
except urllib2.URLError, e:
    print e.reason
    
#禁止访问
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason

#处理异常
req2 = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req2)
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"
