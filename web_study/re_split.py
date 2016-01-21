# -*- coding: cp936 -*-
import re

#�����ܹ�ƥ����Ӵ���string�ָ�󷵻��б�
pattern = re.compile(r'\d+')
print "the split : "+str(re.split(pattern,'one1two2three3four4'))

# ����string�����б���ʽ����ȫ����ƥ����Ӵ�
pattern1 = re.compile(r'\d+')
print "the findall : "+str(re.findall(pattern1,'one1two2three3four4'))

#����string������һ��˳�����ÿһ��ƥ������Match���󣩵ĵ�����
pattern2 = re.compile(r'\d+')
for m in re.finditer(pattern2,'one1two2three3four4'):
    print "the finditer is "+str(m.group())


#ʹ��repl�滻string��ÿһ��ƥ����Ӵ��󷵻��滻����ַ�������repl��һ���ַ���ʱ������ʹ��\id��\g��\g���÷��飬������ʹ�ñ��0��
pattern3 = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print re.sub(pattern3,r'\2 \1', s)
 
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
 
print re.sub(pattern,func, s)

#���� (sub(repl, string[, count]), �滻����)
pattern4 = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print re.subn(pattern4,r'\2 \1', s)
 
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
 
print re.subn(pattern,func, s)
