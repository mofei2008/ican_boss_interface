from selenium import webdriver
import unittest
from business.login_H5_business import login_H5_business
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread

def test_login_email1(name,server_address):
    print(name)
    driver = webdriver.Remote(
        command_executor=server_address,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.get("http:www.baidu.com")

def test_login_email2(name,server_address):
    print(name)
    driver = webdriver.Remote(
        command_executor=server_address,
        desired_capabilities=DesiredCapabilities.FIREFOX
    )
    driver.get("http:h5advisor.haitoutech.com/")

def test_login_email3(name,server_address):
    print(name)
    driver = webdriver.Remote(
        command_executor=server_address,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.get("http:mail.163.com/")

address = {
    "win7": "http://192.168.0.103:4444/wd/hub",
    "win10": "http://192.168.0.104:4444/wd/hub",
    # "cenos8": "http://192.168.0.112:4444/wd/hub"
}
threads = []

for name, url in address.items():
    if name == "win7":
        t = Thread(target=test_login_email1,args=(name,url))
    elif name == 'win10':
        t = Thread(target=test_login_email2,args=(name,url))
    else:
        t = Thread(target=test_login_email3,args=(name,url))
    threads.append(t)
for t in threads:
    t.start()