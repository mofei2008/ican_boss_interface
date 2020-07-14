#!/usr/bin/python
# -*- coding: UTF-8 -*-
import records
from oper import read_Config
import xlrd
import filePath
import os
config = read_Config.ReadConfig()
host = config.get_config_str('DATABASE', 'host')
# port = config.get_config_int('DATABASE', 'port')
port = config.get_config_str('DATABASE', 'port')  # 这里端口号因为是跟其他参数一个整体，都是str型
user = config.get_config_str('DATABASE', 'user')
password = config.get_config_str('DATABASE', 'password')
dbname = config.get_config_str('DATABASE', 'dbname')
charset = config.get_config_str('DATABASE', 'charset')
table = config.get_config_str('DATABASE', 'table')

# # 获取数据库
# db = records.Database('mysql+pymysql://root:@localhost:3306/dev01_git')
# db_url = 'mysql+pymysql://' + user + ':' + passwd + '@' + str(host) + ':' + str(port) + '/' + db
# connect = records.Database('mysql+pymysql://用户名:密码@sqlURl:sql端号/库名')
# db = records.Database(db_url,connect_args={'charset' : 'utf8'})
db_url = 'mysql+pymysql://' + user + ':' + password + '@' + host + ':' + port + '/' + dbname + '?' + 'charset' + '=' + charset

path = filePath.get_Path()
xPath = os.path.join(path, "test_data", 'test_data.xlsx')

def db_read(table):
    db = records.Database(db_url)
    # 查询
    # data = {
    #     'name': '李德涛',
    #     'income': 6000
    # }
    # rows = db.query('select * from test_data where name = "李德涛";')
    # sql = "SELECT * FROM " +  table + " limit 0,2" #只去前几条
    sql = "SELECT * FROM " +  table

    try:
        rows = db.query(sql)
        data = rows.all(as_dict=True)
        return data
    except Exception as ex:
        print("*" * 10, "Error Occured", "*" * 10)
        print(str(ex))
    # rows = db.query(
    #      "SELECT * FROM " + table + " WHERE name=:name and income=:income",
    #     **data)
    #RecordCollection.dataset  输出格式化的数据
    # print('格式化类型输出：',  rows.dataset)
    # print('格式化类型输出：')
    # print(rows.dataset)
    # #RecordCollection.all() 将所有行输出为一个列表，每一行为 Record 类型的实例
    # print('输出所有：',rows.all())
    # #可以加入as_dict=True 输出为字典
    print('输入为字典',rows.all(as_dict=True))
    # #可以加入as_dict=True 输出为字典
    # print('输入为有序字典',rows.all(as_ordereddict=True))
    # # print(rows.all().encode('utf-8').decode('unicode_escape'))
    # #导出为excel
    # xlsx_rows = rows.export('xlsx')
    # # xlsx = xlsx_rows.encode()
    # with open('test.xlsx','wb') as f:
    #     f.write(xlsx_rows)

def db_read_max():

    db = records.Database(db_url)
    # 查询
    data = {
        'name': '李德涛',
        'income': 6000
    }
    # rows = db.query('select * from test_data where name = "李德涛";')
    rows = db.query(
        # "SELECT * FROM " + table + " WHERE name=:name and income=:income",
        "SELECT * FROM " + table,
        **data)
    #RecordCollection.dataset  输出格式化的数据
    # print('格式化类型输出：',  rows.dataset)
    print('格式化类型输出：')
    print(rows.dataset)
    #RecordCollection.all() 将所有行输出为一个列表，每一行为 Record 类型的实例
    print('输出所有：',rows.all())
    #可以加入as_dict=True 输出为字典
    print('输入为字典',rows.all(as_dict=True))
    #可以加入as_dict=True 输出为字典
    print('输入为有序字典',rows.all(as_ordereddict=True))
    # print(rows.all().encode('utf-8').decode('unicode_escape'))
    #导出为excel
    xlsx_rows = rows.export('xlsx')
    # xlsx = xlsx_rows.encode()
    with open('test.xlsx','wb') as f:
        f.write(xlsx_rows)

def db_insert1():
    # # 获取数据库
    # db = records.Database('mysql+pymysql://root:@localhost:3306/dev01_git')
    # db_url = 'mysql+pymysql://' + user + ':' + passwd + '@' + str(host) + ':' + str(port) + '/' + db
    print(db_url)
    # connect = records.Database('mysql+pymysql://用户名:密码@sqlURl:sql端号/库名')
    # db = records.Database(db_url,connect_args={'charset' : 'utf8'})
    db = records.Database(db_url)
    # 新增单条数据

    data = {
        'case_des': '手机号正确的账户密码',
        'doc': 'haitou-user/user/loginByMobile',
        'code': 'code',
        'result': '0000',
        'method_type': 'post',
        'par': '{"mobile":"18610806332","password":"Aa111111","regionalCode":"+86","userType":"1","clt":"h5Wealth"}'
    }
    # rows = db.query('select * from test_data where name = "李德涛";')
    db.query(
        "INSERT INTO " + table + " (case_des, doc,code,result,method_type,par) values (:case_des, :doc , :code, :result,:method_type,:par)",
        **data)


def db_insert(name,income):
    # # 获取数据库
    # db = records.Database('mysql+pymysql://root:@localhost:3306/dev01_git')
    # db_url = 'mysql+pymysql://' + user + ':' + passwd + '@' + str(host) + ':' + str(port) + '/' + db
    print(db_url)
    # connect = records.Database('mysql+pymysql://用户名:密码@sqlURl:sql端号/库名')
    # db = records.Database(db_url,connect_args={'charset' : 'utf8'})
    db = records.Database(db_url)
    # 新增单条数据
    data = {
        'name': name,
        'income': income
    }
    # rows = db.query('select * from test_data where name = "李德涛";')
    db.query(
        "INSERT INTO " + table + " (name, income) values (:name, :income)",
        **data)
    # # 新增多条数据
    # users = [
    #     {'name': 'ldt1', 'income': '1000'},
    #     {'name': 'ldt2', 'income': '2000'},
    #     {'name': 'ldt3', 'income': '3000'},
    #     {'name': 'ldt4', 'income': '4000'}
    # ]
    # db.bulk_query(
    #     "INSERT INTO " + table + "(name, income) values (:name, :income)",
    #     users)

def db_create():
    print(db_url)
    # connect = records.Database('mysql+pymysql://用户名:密码@sqlURl:sql端号/库名')
    # db = records.Database(db_url,connect_args={'charset' : 'utf8'})
    db = records.Database(db_url)
    sql = """create table usertest (userid int primary key,username varchar(50));"""
    db.query(sql)

def db_excel():
    db = records.Database(db_url)
    book = xlrd.open_workbook(xPath)
    sheet = book.sheet_by_name("login")
    rows = sheet.nrows
    for r in range(1,rows):
        case_des = sheet.cell(r, 0).value
        doc = sheet.cell(r, 1).value
        code = sheet.cell(r, 2).value
        result = sheet.cell(r, 3).value
        type = sheet.cell(r, 4).value
        par = sheet.cell(r, 5).value
        data = {
            'case_des': case_des ,
            'doc': doc,
            'code': code,
            'result': result,
            'method_type': type,
            'par': par
        }
        print(data)
        try:
            # db.query("INSERT INTO login  (case_des, doc,code,result,method_type,par) values (:case_des, :doc,:code,:result,:method_type,:par)",data)
            db.query(
                "INSERT INTO login  (case_des, doc,code,result,method_type,par) values (:case_des, :doc , :code, :result,:method_type,:par)",
                **data)

        except Exception as ex:
            print("*" * 10, "Error Occured", "*" * 10)
            print(str(ex))

def db_transaction():
    db = records.Database(db_url)
    conn = db.get_connection()
    tx = conn.transaction()
    try:
        conn.query("INSERT INTO test_data(name, income) values('ldt5', '50000')")
        conn.query("INSERT INTO test_data(name, income) values('ldt6', ' 60000')")

        # conn.query("INSERT INTO test_data(name, income) values('ldt61fffffffffffffffffffffffffffffffffffffffffffffffffff', '6000000000000000000000000000000')")
        tx.commit()
    except Exception as ex:
        print("*" * 10, "Error Occured", "*" * 10)
        print(str(ex))
        tx.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    db_insert('aaa','6666')