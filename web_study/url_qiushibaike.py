# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time

page = 4
url = 'http://www.qiushibaike.com/hot/page/' + str(page)+'/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    #print "the type is "+str(type(content))
    pattern = re.compile('<div.*?author clearfix">.*?<a.*?<h2>(.*?)</h2>.*?content">'+
                         '(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number hidden">(.*?)</span>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            x_data=time.localtime(int(item[2]))
            res_data=time.strftime('%Y-%m-%d %H:%M:%S',x_data)
            print item[0],item[1],res_data,item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
