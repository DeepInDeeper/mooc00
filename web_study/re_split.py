# -*- coding: cp936 -*-
import re

#按照能够匹配的子串将string分割后返回列表
pattern = re.compile(r'\d+')
print "the split : "+str(re.split(pattern,'one1two2three3four4'))

# 搜索string，以列表形式返回全部能匹配的子串
pattern1 = re.compile(r'\d+')
print "the findall : "+str(re.findall(pattern1,'one1two2three3four4'))

#搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器
pattern2 = re.compile(r'\d+')
for m in re.finditer(pattern2,'one1two2three3four4'):
    print "the finditer is "+str(m.group())


#使用repl替换string中每一个匹配的子串后返回替换后的字符串。当repl是一个字符串时，可以使用\id或\g、\g引用分组，但不能使用编号0。
pattern3 = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print re.sub(pattern3,r'\2 \1', s)
 
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
 
print re.sub(pattern,func, s)

#返回 (sub(repl, string[, count]), 替换次数)
pattern4 = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print re.subn(pattern4,r'\2 \1', s)
 
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
 
print re.subn(pattern,func, s)
