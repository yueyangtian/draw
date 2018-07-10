#! /bin/python
# -*- coding: utf-8 -*-
#sheet1.write(0,0,'0,0,');
#sheet1.write(0,1,'0,1,');
#sheet1.write(0,2,'0,2,');
import xlwt
from xlwt import Workbook

book = Workbook(encoding='utf-8')
sheet1 = book.add_sheet('Sheet1')

sheet1.write(0,0,u'端口');
sheet1.write(0,1,u'限制');
sheet1.write(0,2,u'使用');
sheet1.write(0,3,u'剩余');
#read json
f = file('traffic.tmp')
index = 1
for line in open('traffic.tmp'):
    s1=line.split()
    print line
    if s1[0]=='#':
        continue
    if s1[0]=='8888':
        continue

    sheet1.write(index,0,s1[0])
    sheet1.write(index,1,s1[1])
    sheet1.write(index,2,s1[2])
    sheet1.write(index,3,s1[3])
    index = index + 1
    line = f.readline()
book.save('test_tar.xls')
