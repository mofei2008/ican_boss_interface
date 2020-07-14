import pymysql
from random import randint
from oper import read_Config
config = read_Config.ReadConfig()
#连接数据库
# db_connect = pymysql.connect("localhost","3306","root","123","test",'utf8')
# cursor = db_connect.cursor()
host = config.get_config_str('DATABASE', 'host')
port = config.get_config_int('DATABASE', 'port')
user = config.get_config_str('DATABASE', 'user')
password = config.get_config_str('DATABASE', 'password')
db = config.get_config_str('DATABASE', 'db')
charset = config.get_config_str('DATABASE', 'charset')
table = config.get_config_str('DATABASE', 'table')
db = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
cursor = db.cursor()

#通过循环语句插入数据
number = 1
name = 0
for i in range(10):
    number = number + 1
    name = name + 1
    student_idnumber ="xh0000%d"%(number)#实现自增，数据不能重复
    names = "李一%d"%(name)#实现自增，数据不能重复
    #括号中的%s要加上单引号，换行用\分隔，
    sql = "insert into persons \
    (student_id,name,id_card,sex,age,achievement,adress) \
    values ('%s', '%s', '%s', '%s', '%s','%s','%s')" % \
    (student_idnumber,names,'120100199907224349','女','39','309','天津市市辖区')

    try:
        cursor.execute(sql)#执行
        db.commit()#提交
    except:
        db.rollback()#发生错误时回滚

    cursor.execute(sql)
    db.commit()
db.close()