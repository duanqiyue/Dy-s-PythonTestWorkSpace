# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def mail():
    sender = 'duanqiyue666@163.com'
    receiver = '1151044240@qq.com'
    subject = 'SMTP测试SendEmal发送邮件........'
    username = 'duanqiyue666@163.com'
    password = 'ai812380163'

    msg = MIMEText('SMTP测试SendEmal发送邮件\r\nSMTP测试SendEmal发送邮件', 'plain', 'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = '段奇越<duanqiyue666@163.com>'
    msg['To'] = receiver
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print "成功"

