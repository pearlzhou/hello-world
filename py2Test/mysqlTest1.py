# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 下午9:20
# @Author  : zhouzz
# @FileName: mysqlTest1.py

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     db='pearl')

# 使用 cursor() 方法创建一个游标对象cur
cur = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cur.execute("select name, psw from user")

# 使用 fetchall() 方法获取查询结果
data = cur.fetchall()

print(data)

# 关闭数据库连接
cur.close()
db.close()