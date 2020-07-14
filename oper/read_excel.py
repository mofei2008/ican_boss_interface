#coding=utf-8
#!usr/bin/python
import xlrd
#from xlutils.copy import copy
import filePath
import os
path = filePath.get_Path()

class XLDatainfo(object):
    def __init__(self,path = None):
        self.x1 = xlrd.open_workbook(path)

    def get_sheetinfo_by_name(self,sheetname):
        self.sheet = self.x1.sheet_by_name(sheetname)
        print(self.sheet)
        return self.get_sheet_info()


    def get_sheet_info(self):
        self.rows = self.sheet.nrows
        infolist = []
        for row in range(1,self.rows):
            info = self.sheet.row_values(row)
            infolist.append(info)
        return infolist

    def get_sheet_data(testfile,sheetname):
        xlsPath = os.path.join(path, "test_data",testfile)
        datainfo = XLDatainfo(xlsPath)
        Data = datainfo.get_sheetinfo_by_name(sheetname)
        return Data
    # def get_sheet_data(testfile, sheetname):
    #     datainfo = XLDatainfo(r'E:\Test\Haitou\test_data\%s' % testfile)
    #     Data = datainfo.get_sheetinfo_by_name(sheetname)
    #     return Data

    def write_data(self,row,value):
        data = self.x1
        write_data = copy(data)
        write_data.get_sheet(0).write(row,7,value)
        print(write_data)
        write_data.save(r'E:\Test\Haitou\test_data\keywords.xlsx' )



if __name__ =="__main__":
    # datainfo = XLDatainfo(r'E:\Test\Haitou\test_data\test_data.xlsx')
    # alldata = datainfo.get_sheetinfo_by_name('H5')
    # print(alldata)
    # x1 = XLDatainfo
    # testfile = 'test_data.xlsx'
    # H5 = x1.get_sheet_data('test_data.xlsx', 'H5')
    # print(H5)c
    print(XLDatainfo.get_sheet_data('test_data.xlsx','login'))