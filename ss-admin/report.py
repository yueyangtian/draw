#!/usr/bin/python
# -*- coding: UTF-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import xlwt
from xlwt import Workbook
import smtplib
import threading
import time
def sendEmail(to_addr):

    from_addr = u'pawnsir@163.com'  # 输入邮箱地址和口令
    password = u'tyy1038910619'
    #to_addr = ['belinda.0422@hotmail.com']  # 输入邮箱收件人地址
    #to_addr = ['1038910619@qq.com']  # 输入邮箱收件人地址

    smtp_server = 'smtp.163.com'  # 输入SMTP服务器地址

    msg = MIMEMultipart()
    msgContent = u'hi, yestoday report is here'
    msg.attach(MIMEText(msgContent, 'plain', 'utf-8'))
    msg['Subject'] = 'VPN Work Rep'
    msg['Content-Type'] = 'Text/HTML'
    msg['From'] = from_addr
    msg['to']=';'.join(to_addr)

    part = MIMEApplication(open('test_tar.xls','rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="foo.xls")
    msg.attach(part)

    try:
        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print 'Send Success'

    except smtplib.SMTPException, e:
        print 'Send Failed, %s' % e
def flushXls():
    
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('Sheet1')
    
    sheet1.write(0,0,u'端口');
    sheet1.write(0,1,u'限制');
    sheet1.write(0,2,u'使用');
    sheet1.write(0,3,u'剩余');
    #read json
    f = file('sstraffic')
    index = 1
    for line in open('sstraffic'):
        s1=line.split()
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
def reportTimer():
    print 'start...'
    flushXls()
    f = file('report.config')
    for line in open('report.config'):
        print '*************************************************************************************************'
        print 'Send:'+line
        sendEmail(line)
        line = f.readline()
    timer = threading.Timer(20,reportTimer)
    timer.start()
if __name__ == "__main__":
    reportTimer()





