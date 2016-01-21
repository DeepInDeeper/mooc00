import urllib2

requst=urllib2.Request("http://baidu.com")
response=urllib2.urlopen(requst)
print response.read()
