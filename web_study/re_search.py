# -*- coding: cp936 -*-
#����reģ��
import re

# ��������ʽ�����Pattern����
pattern = re.compile(r'world')
# ʹ��search()����ƥ����Ӵ�����������ƥ����Ӵ�ʱ������None
# ���������ʹ��match()�޷��ɹ�ƥ��
match = re.search(pattern,'hello world!')
if match:
    # ʹ��Match��÷�����Ϣ
    print match.group()
