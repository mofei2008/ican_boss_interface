from selenium import webdriver
import unittest
from business.login_H5_business import login_H5_business
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread

address = {
    "win7": "http://192.168.0.103:4444/wd/hub",
    "win10": "http://192.168.0.104:4444/wd/hub",
    # "cenos8": "http://192.168.0.112:4444/wd/hub"
}

print('开始执行测试用例：')

def test_login_email(name,server_address):
    print(name)
    driver = webdriver.Remote(
        command_executor=server_address,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    url = 'https://h5advisor.haitoutech.com/'
    driver.get(url)  # 打开百度页面
    driver.maximize_window()
    loginh5 = login_H5_business(driver)
    loginh5.login_email('lidetao@163.com','Aa111111')
    driver.quit()

def test_login_mobile(name,server_address):
    print(name)
    driver = webdriver.Remote(
        command_executor=server_address,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    url = 'https://h5advisor.haitoutech.com/'
    driver.get(url)  # 打开百度页面
    driver.maximize_window()
    loginh5 = login_H5_business(driver)
    loginh5.login_mobile('18610806332','Aa111111')
    driver.quit()

threads = []

for name, url in address.items():
    if name == "win7":
        t = Thread(target=test_login_email,args=(name,url))
    elif name == 'win10':
        t = Thread(target=test_login_mobile,args=(name,url))
    else:
        t = Thread(target=test_login_mobile,args=(name,url))
    threads.append(t)
for t in threads:
    t.start()



#
# def test_login_email1(name,server_address):
#     print(name)
#     driver = webdriver.Remote(
#         command_executor=server_address,
#         desired_capabilities=DesiredCapabilities.CHROME
#     )
#     driver.get("http:www.baidu.com")
#
# def test_login_email2(name,server_address):
#     print(name)
#     driver = webdriver.Remote(
#         command_executor=server_address,
#         desired_capabilities=DesiredCapabilities.FIREFOX
#     )
#     driver.get("http:h5advisor.haitoutech.com/")
#
# def test_login_email3(name,server_address):
#     print(name)
#     driver = webdriver.Remote(
#         command_executor=server_address,
#         desired_capabilities=DesiredCapabilities.CHROME
#     )
#     driver.get("http:mail.163.com/")