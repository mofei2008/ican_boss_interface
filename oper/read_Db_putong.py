#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
import threading
import time
from oper import read_Config
config = read_Config.ReadConfig()
# 打开数据库连接（ip/端口/数据库用户名/登录密码/数据库名/编码）
# db = pymysql.connect(host="localhost", port=3306, user="root", password="123", db="test", charset='utf8')
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # 使用 execute()  方法执行 SQL 查询（查询mysql的版本）
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print("Database version : %s " % data)
# # 关闭数据库连接
# db.close()


# encoding=utf-8
def db_ins():
    try:
        host = config.get_config_str('DATABASE', 'host')
        port = config.get_config_int('DATABASE', 'port')
        user = config.get_config_str('DATABASE', 'user')
        password = config.get_config_str('DATABASE', 'password')
        db = config.get_config_str('DATABASE', 'db')
        charset = config.get_config_str('DATABASE', 'charset')
        table = config.get_config_str('DATABASE', 'table')
        db = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)  # 注意这里是utf8
        cursor = db.cursor()

        id =   11
        name = 's'
        age =  '1'
        sex =  '2'
        income = 1121212
        # params = [id,name,age,sex,income]
        params = [id,name,age,sex,income]

        count=cursor.execute("insert into test_data(id,name,age,sex,income) values(%s,%s,%s,%s,%s)",params)
        print(count)
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print(e.message)

def db_canshuhua():
    try:
        host = config.get_config_str('DATABASE', 'host')
        port = config.get_config_int('DATABASE', 'port')
        user = config.get_config_str('DATABASE', 'user')
        password = config.get_config_str('DATABASE', 'password')
        db = config.get_config_str('DATABASE', 'db')
        charset = config.get_config_str('DATABASE', 'charset')
        table = config.get_config_str('DATABASE', 'table')
        db = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)  # 注意这里是utf8
        cursor = db.cursor()

        id =   input('请输入学生id：')
        name = input('请输学生姓名：')
        age =  input('请输入学生年龄：')
        sex =  input('请输入学生性别：')
        income = input('请输入学生收入：')
        params = [id,name,age,sex,income]
        count=cursor.execute( "insert into test_data(id,name,age,sex,income) values(%s,%s,%s,%s,%s)",params)
        print("ID of last record is ", int(cursor.lastrowid) ) # 最后插入行的主键ID
        print("ID of inserted record is ", int(db.insert_id()) ) # 最新插入行的主键ID，conn.insert_id()一定要在conn.commit()之前，否则会返回0
        # print(count)
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print('报错了！')

def db_version():
    host = config.get_config_str('DATABASE', 'host')
    port = config.get_config_int('DATABASE', 'port')
    user = config.get_config_str('DATABASE', 'user')
    password = config.get_config_str('DATABASE', 'password')
    db = config.get_config_str('DATABASE', 'db')
    charset = config.get_config_str('DATABASE', 'charset')
    table = config.get_config_str('DATABASE', 'table')

    db = pymysql.connect(host = host,port=port,user=user, password=password,db=db,charset=charset)#
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    print('DataBase version: %s' %data + now)
    db.close()
    # timer = threading.Timer(5, db_timer)
    # timer.start()

def db_read():
    host = config.get_config_str('DATABASE', 'host')
    port = config.get_config_int('DATABASE', 'port')
    user = config.get_config_str('DATABASE', 'user')
    password = config.get_config_str('DATABASE', 'password')
    db = config.get_config_str('DATABASE', 'db')
    charset = config.get_config_str('DATABASE', 'charset')
    table = config.get_config_str('DATABASE', 'table')

    db = pymysql.connect(host = host,port=port,user=user, password=password,db=db,charset=charset)#注意这里是utf8
    cursor = db.cursor()
    #没有该表
    # sql = "select * from ccc"
    # c.execute("SELECT * FROM foo WHERE bar = %s AND baz = %s", (param1, param2))
    # sql = "select * from {table} where sex = 'M'".format(table=table)
    sex = 'F'
    sql = "select * from test_data where sex = %s",(sex)

    try:
        cursor.execute(sql)

        data = cursor.fetchall()
        now = time.strftime('%Y-%m-%d %H_%M_%S')
        print(data )
        for row in data:
            name = row[0]
            age = row[1]
            sex = row[2]
            income = row[3]
            print("name=%s,age=%d,sex=%s,income=%d"%\
                  (name,age,sex,income))
    #如果没有该表，提示无数据
    except:
        print('Error:no this table!1')
    db.close()

def db_update():
    host = config.get_config_str('DATABASE', 'host')
    port = config.get_config_int('DATABASE', 'port')
    user = config.get_config_str('DATABASE', 'user')
    password = config.get_config_str('DATABASE', 'password')
    db = config.get_config_str('DATABASE', 'db')
    charset = config.get_config_str('DATABASE', 'charset')
    table = config.get_config_str('DATABASE', 'table')

    db = pymysql.connect(host = host,port=port,user=user, password=password,db=db,charset=charset)#注意这里是utf8
    cursor = db.cursor()
    #没有该表
    # sql = "select * from ccc"
    # c.execute("SELECT * FROM foo WHERE bar = %s AND baz = %s", (param1, param2))
    sql = "update {table} set income = 100000 where sex = 'F'"
    try:
        cursor.execute(sql)
        db.commit()
        print('已更新！')
    #如果没有该表，提示无数据
    except:
        db.rollback()
        print('已回滚！2')
    db.close()

def db_insert():
    host = config.get_config_str('DATABASE', 'host')
    port = config.get_config_int('DATABASE', 'port')
    user = config.get_config_str('DATABASE', 'user')
    password = config.get_config_str('DATABASE', 'password')
    db = config.get_config_str('DATABASE', 'db')
    charset = config.get_config_str('DATABASE', 'charset')
    table = config.get_config_str('DATABASE', 'table')

    db = pymysql.connect(host = host,port=port,user=user, password=password,db=db,charset=charset)#注意这里是utf8
    cursor = db.cursor()
    #没有该表
    # sql = "select * from ccc"
    # c.execute("SELECT * FROM foo WHERE bar = %s AND baz = %s", (param1, param2))
    # keys = {'id','name','age','sex','income'}
    # values = {7,'赵1',20,'M',6000}
    data = {
        'id':7,
        'name':'赵1',
        'age':20,
        'sex':'M',
        'income':6000
    }
    sql = 'INSERT INTO  {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)
    # sql = """INSERT INTO test_data(id,name,
    #          age, sex,income)
    #          VALUES (8,'赵2', 20, 'M', 32000)"""

    # sql = "insert into test_data(name,age,sex,income)\
    #       values ('赵六'，'50','m','6000')"
    try:
        cursor.execute(sql)
        db.commit()
        print('已更新！')
    #如果没有该表，提示无数据
    except:
        db.rollback()
        print('已回滚！3')
    db.close()
# def create_table():
#     import pymysql
#     # 打开数据库连接
#     db = pymysql.connect(host="localhost", port=3306, user="root", password="root", db="test", charset='utf8')
#     # 使用cursor()方法获取操作游标
#     cursor = db.cursor()
#     # 创建数据表SQL语句
#     sql = 'select * from test'
#     # sql = """
#     # create table `xixi`(`names` varchar(255) default null,
#     # `age` int(3) default null,
#     # `income` decimal(8,2) default 0)
#     # ENGINE=InnoDB DEFAULT charset=utf8;
#     # """
#     # sql = """CREATE TABLE EMPLOYEE (
#     #          FIRST_NAME  CHAR(20) NOT NULL,
#     #          LAST_NAME  CHAR(20),
#     #          AGE INT,
#     #          SEX CHAR(1),
#     #          INCOME FLOAT )"""
#     try:
#
#         # 执行sql语句
#
#         cursor.execute(sql)
#
#         # 提交到数据库执行
#
#         db.commit()
#
#     except:
#
#         # 如果发生错误则回滚
#
#         db.rollback()
#
#     # 关闭数据库连接
#
#     db.close()
#

if __name__ == "__main__":
    db_canshuhua()