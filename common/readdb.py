#coding:utf-8
import pymysql
from common.readConfig import Readconfig
a = Readconfig()
testuser = a.get_db('testuser')
localhost = a.get_db('localhost')
testpassword = a.get_db('testpasswoed')
dbname = a.get_db('dbname')
print(testuser,testpassword,dbname)
# 连接数据库
db = pymysql.connect(host=localhost,user=testuser,passwd=testpassword,port=3306,db=dbname,charset='utf8')
# 生成游标对象
cursor = db.cursor()
# SQL语句
sql = "select * from user"
# 执行SQL语句
cursor.execute(sql)
# 通过fetchall方法获得数据
data = cursor.fetchall()
print(data)
# 关闭游标
cursor.close()
# 关闭连接
db.close()