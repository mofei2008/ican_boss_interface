# coding=utf-8
# !usr/bin/python
from ddt import ddt,data,unpack
import unittest
import requests
import json
from public import base
# from oper import read_Config
# from oper import read_excel
# testcasefile = 'test_data.xlsx'
# product = read_excel.XLDatainfo.get_sheet_data(testcasefile,'product')

@ddt
class Test_EmpList(unittest.TestCase):
    '''员工列表'''
    def setUp(self) :
        self.host = 'https://pbsapi.aikenong.com.cn/boss/'
        self.token = base.get_token_akn()
        self.header = {'Authorization': "JWT " + self.token}

    def test01_emplist(self):
        '''员工列表'''
        doc = "custom/emplist/105710052/"
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        # json_str = company.content.decode()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()