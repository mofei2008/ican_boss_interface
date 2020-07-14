
# coding=utf-8
# !usr/bin/python
from ddt import ddt,data,unpack
import unittest
from public import base
from oper import read_Config
from oper import read_excel
# testcasefile = 'test_data.xlsx'
# product = read_excel.X
# LDatainfo.get_sheet_data(testcasefile,'product')

@ddt
class Test_Login(unittest.TestCase):
    '''登录功能'''
    def setUp(self) :
        self.url = 'https://pbsapi.aikenong.com.cn/boss/login/'
    @data(['13611112222','akn2019666','httpCode',200],['13611112222','akn2019666','msg','登录成功'],['13611112222','2121212','code',["400"]])
    @unpack
    def test_login(self,username,password,code,result):
        '''登录功能'''
        print('测试开始！')
        par = {"username": username, "password": password}
        resp = base.method(self.url,method='post',data=par)
        # print(resp)
        code1 = resp[code]
        print(code1)
        print(resp)
        self.assertEqual(code1,result,msg= '返回值错误')
        print('测试完成！')

    def tearDown(self):
        pass
