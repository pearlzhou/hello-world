# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 下午6:40
# @Author  : zhouzz
# @FileName: index.py

import cgi
import MySQLdb as sql

data = cgi.FieldStorage() #用来接受请求数据
if data.has_key('userTime'):
	value = data['userTime'].value
else:
	value = 'not Found' #容错处理
con = sql.connect(user = 'root', passwd = '123', db= '', host = 'localhost')

cur = con.cursor()
cur.execute('insert into cpu vaule ('1','%s');'%value)

con.commit()
cur.close()
con.close()