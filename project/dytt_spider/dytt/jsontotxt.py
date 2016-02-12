import json
import os
 
data = []
with open('movies_data.json') as f:
  for line in f:
    data.append(json.loads(line))
 

 
 
import codecs
file_object = codecs.open('movies_data.txt', 'w' ,"utf-8")
str = "\r\n"
splitstr = "#_#"
for item in data:
  for n in  range(len(item['link'])):
    str = "%s the title is %s    the URL is: http://www.dytt8.net/%s\r\n" % (n,item['dyName'][n],item['link'][n])
    file_object.write(str)
 

file_object.close()
print "success"
