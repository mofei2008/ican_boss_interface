#coding=utf-8
#!usr/bin/python
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from oper import read_Config
import json
import filePath
import os
path = filePath.get_Path()
xPath = os.path.join(path, "test_data", 'login.json')

def send_mail(filename):

    #定义邮件标题
    # mail_host = 'smtp.qiye.163.com'
    # mail_user = 'detao.li@haitouglobal.com'
    # mail_pass = '#*LDTSDNMM11'
    # sender = 'detao.li@haitouglobal.com'

    # mail_host = ('smtp.qq.com')
    # mail_user = '363613636@qq.com'
    # mail_pass = 'ejnxuvntlzjecajd'
    # sender = '363613636@qq.com'
    # receivers = ['363613636@qq.com','lidetao@163.com']
    mail_config = read_Config.ReadConfig()
    mail_host = mail_config.get_config_str('EMAIL','mail_host')
    print(mail_host)
    # mail_user = mail_config.get_config('EMAIL','mail_user')
    mail_pass = mail_config.get_config_str('EMAIL','mail_pass')
    sender = mail_config.get_config_str('EMAIL','sender')
    # receivers1 = mail_config.get_config_str('EMAIL','receivers1')
    # receivers2 = mail_config.get_config_str('EMAIL','receivers2')
    receivers = mail_config.get_config_str('EMAIL','receivers')
    receivers1 = "363613636@qq.com"
    receivers2 = "lidetao@163.com"
    receivers = eval(receivers)
    print(receivers)
    message=MIMEMultipart('related')
    #读取报告
    f=open(filename,'rb')
    mail_body = f.read()
    att = MIMEText(mail_body,'base64','utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="report.html"'
    message.attach(att)
    f.close()
    #定义邮件正文，报告以正文的形式发送
    msg = MIMEText(mail_body,'html','utf-8')
    message.attach(msg)
    message['From']=sender
    message['To']=','.join(receivers)
    print(message['To'])
    message['Subject']=Header(mail_config.get_config_str('EMAIL','subject'),'utf-8')
    smtp=smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(sender,mail_pass)
    smtp.sendmail(sender,receivers,message.as_string())
    smtp.quit()
    # print("测试报告邮件已发送至" + json.dumps(receivers))
    print("测试报告邮件已发送至" + str(receivers))
    print("email has send out")

if __name__ == '__main__':
    send_mail(xPath)