#coding=utf-8
#!usr/bin/python
import configparser

from public import Config
from oper import read_excel
import requests,json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# import configparser
import os
import filePath
import time
import urllib3

path = filePath.get_Path()
def get_url(doc):
    host = Config.url()
    doc = doc
    url = ''.join([host,doc])
    return url

def get_sheet_data(testfile,sheetname):
    xlsPath = os.path.join(path, "test_data",testfile)
    datainfo = read_excel.XLDatainfo(xlsPath)
    Data = datainfo.get_sheetinfo_by_name(sheetname)
    return Data
# def get_sheet_data1(testfile,sheetname):
#     datainfo = read_excel1.XLDatainfo(r'E:\Test\Haitou\test_data\%s' %testfile)
#     Data = datainfo.get_sheetinfo_by_name(sheetname)
#     return Data

# def get_1sheet_data(self,testfile, sheetname):
#     datainfo = ExcelUtil(r'E:\Test\Haitou\test_data\%s' % testfile)
#     Data = datainfo.get_sheetinfo_by_name(sheetname)
# # def get_response(url,Method,**DataALL)
#     if Method == 'get':
#         resp = HttpService.MyHTTP().get(url,**DataALL)
#     elif Method == 'post':
#         resp = HttpService.MyHTTP().post(url,**DataALL)
#     return resp
def report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"/"+fn))
    filename = os.path.join(testreport,lists[-1])
    print("报告已生成：%s" % filename)
    return filename

def fp():
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    # filename = './report/' + now + '_result.html'
    report_name = now + '_result.html'
    print(report_name)
    filename = os.path.join(path,'report',report_name)
    print(filename)
    return filename

def get_value1(server,host):
    file_path = r'E:\Test\Haitou\public\server.ini'
    print(file_path)
    cf = configparser.ConfigParser()
    cf.read(file_path)
    data = cf.get(server,host)
    print(data)

def read_jsondata(id):
    with open('E:/Test/Haitou/test_data/login.json', encoding='utf-8') as fp:
        data = json.load(fp)
        a = data[id]
        return a

def send_post(url, data):
    """ 定义send_post函数，用来接收参数，发送post请求 """
    r = requests.post(url=url, data=data)
    result = r.json()
    return result

def get_ProId(data):
    url = 'https://api.haitoutech.com/haitou-product/product/dailyProductList'
    # url = ''.join([host, doc])
    # par = {'clt':clt,'returnType':returnType,'productType':productType,'token':token}
    resp = requests.post(url,data=data)
    r = resp.json()
    # print(r)
    return r

def download_file():
    url = 'https://www.imooc.com/mobile/appdown'
    # token = base.get_token_ok(doc1, login)
    res = requests.post(url).content
    with open('E:/imooc.apk','wb') as f:
        f.write(res)

    print(res)

def upload_file(token):
    url = 'https://api.haitoutech.com/haitou-order/moneyFund/uploadFile/'
    # token = get_token_ok(doc1, login)
    file = {
        'file': ('bbb.png', open('E:/bbb.png', 'rb'), 'image/png'),
    }
    data = {'clt': 'h5Wealth','token': token}
    r = requests.post(url, files=file, data=data,verify=False).json()
    res = r['data']['filePath']
    print(res)
    return res

def get_ProId1(self,doc1,login):

    par = {'clt':'h5Wealth', 'returnType':'151','productType':'340','token':get_token_ok(doc1,login)}
    r = requests.post(url,data=par,verify=False)
    resp = r.json()
    # print(resp)
    # dd = resp['data']
    # print(dd)
    # aa = dd[1]['id']
    # print(aa)
    return resp

def method(url, method, data):
    """ 定义一个主函数，根据method是get或post，来调用send_post()或send_get() """

    requests.packages.urllib3.disable_warnings()

    if method == 'post':
        res = requests.post(url=url, data=data,verify=False)  # 如果是POST请求，则调用send_post()
        r = res.json()
    else:
        res = requests.get(url=url, data=data,verify=False)  # 如果是GET请求，则调用send_get()
        r = res.json()
    return r  # 将结果返回出去

# def upload_file(self):
#     url1 = 'https://api.haitoutech.com/haitou-order/moneyFund/uploadFile'
#     project_path = os.path.dirname((os.getcwd()))
#     print(project_path)
#     file_path = project_path + '/test_images/'
#     print(file_path)
#     # file_path = './testimages'
#     with open(file_path + 'bbb.png','rb') as f:
#         files = {'files': ('bbb.png', f, 'image/png')}
#         par = {'clt':'h5Wealth','token':get_token_ok()}
#         r = requests.post(url1, data=par,files=files)
#         print(r.content)

def get_token_ok1(doc1,login):
    host = 'https://api.haitoutech.com/haitou-user/user/'
    # doc1 = 'loginByEmail'
    url = ''.join([host, doc1])
    a = login
    resp = requests.post(url, params=a)
    token = resp.json()['data'][0]

    print(token)
    return token

def get_token_ok(doc1,login):
    host = 'https://api.haitoutech.com/haitou-user/user/'
    doc1 = 'loginByEmail'
    url = ''.join([host, doc1])
    a = eval(login)
    resp = requests.post(url, params=a,verify=False)
    token = resp.json()['data']
    print(token)
    return token

def get_token_akn():
    url = 'https://pbsapi.aikenong.com.cn/boss/login/'
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    par = {"username": '13611112222', "password": 'akn2019666'}
    resp = requests.post(url, data=json.dumps(par), headers=headers)
    token = resp.json()['data']['token']
    # token = login()
    print(token)
    return token

def get_token():
    host = 'https://api.haitoutech.com/haitou-user/user/'
    doc1 = 'loginByEmail'
    url = ''.join([host, doc1])
    a = {'email':'lidetao@163.com','password':'Aa111111', 'userType':'1','clt':'h5Wealth'}
    resp = requests.post(url, params=a,verify=False)
    token = resp.json()['data']
    print(token)
    return token

def get_token_not_ok():
    host1 = 'https://api.haitoutech.com/haitou-user/user/'
    doc1 = 'loginByEmail'
    url1 = ''.join([host1, doc1])
    data1 = {'email':'lidetao@163.com','password':'Aa111111', 'userType':'1','clt':'h5Wealth'}
    r1 = requests.post(url1, data=data1)
    token = r1.json()["data"]
    print(token)
    return token

def configpath(filename):
    path = filePath.get_Path()
    config_path = os.path.join(path, 'test_data', filename)
    print(config_path)
    config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
    config.read(config_path, encoding='utf-8')
    return config

def send_mail(filename):
    #定义邮件标题
    # mail_host = 'smtp.qiye.163.com'
    # mail_user = 'detao.li@haitouglobal.com'
    # mail_pass = '#*LDTSDNMM11'
    # sender = 'detao.li@haitouglobal.com'
    mail_host = ('smtp.qq.com')
    mail_user = '363613636@qq.com'
    mail_pass = 'ejnxuvntlzjecajd'
    sender = '363613636@qq.com'
    receivers = ['363613636@qq.com','lidetao@163.com']
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

    message['Subject']=Header('接口自动化测试报告','utf-8')
    smtp=smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(mail_user,mail_pass)
    smtp.sendmail(sender,receivers,message.as_string())
    smtp.quit()
    print("测试报告邮件已发送至" + json.dumps(receivers))
    print("email has send out")

def get_toast_text(self,text):
    try:
        toast_loc = (By.XPATH, "//*[contains(@text,'"+text+"')]")
      #  logger.info(toast_loc)
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
        return ele.text
    except:
        return None

#在测试报告目录下找到最新的报告文件,打印且返回最新报告的名称
# def report(testreport):
#     lists = os.listdir(testreport)
#     lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
#     filename = os.path.join(testreport,lists[-1])
#     print(filename)
#     return filename

# def get_token():
#     host1 = 'https://api.haitoutech.com/haitou-user/user/'
#     doc1 = 'loginByMobile'
#     url1 = ''.join([host1, doc1])
#     data1 = {'mobile': '18610806332',
#              'password': 'Aa111111',
#              'regionalCode': '+86',
#              'userType': '1',
#              'clt': 'h5Wealth'}
#     r1 = requests.post(url1, data=data1)
#     token = r1.json()["data"]
# #    print(token)
#     return token


if __name__ == '__main__':
    print(get_sheet_data('test_data.xlsx','login'))