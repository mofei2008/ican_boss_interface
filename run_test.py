#coding=utf-8
#!usr/bin/python
import unittest
import os
from public import base,HTMLTestRunnerCN
from oper import send_mail
import filePath
from oper import read_Config
import threading
path = filePath.get_Path()

def Run():
    #构建测试集
    test_dir = os.path.join(path, "testcase\\interCase")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    f = base.fp()
    fp = open(f,"wb")
    mail_config = read_Config.ReadConfig()
    title = mail_config.get_config_str('EMAIL','title')
    description = mail_config.get_config_str('EMAIL','description')
    tester = mail_config.get_config_str('EMAIL','tester')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title=title,description=description,verbosity=2,tester=tester)
    runner.run(discover)
    fp.close()
    test_report = os.path.join(path,"report")
    rep = base.report(test_report)
    #发送邮件
    send_mail.send_mail(rep)
    # run = test_case.Run
    # test_dir = os.path.join(path, "testcase")
    # timer = threading.Timer(600, Run)
    # timer.start()

if __name__ =="__main__":
    Run()