# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 下午9:25
# @Author  : zhouzz
# @FileName: selectTest.py

import MySQLdb

def select_db(sql):
	db=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='123456',db='pearl')
	cur = db.cursor()
	cur.execute(sql)
	data = cur.fetchall()
	cur.close()
	db.close()
	return data
def delete_db(sql_delete):
	db=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='123456',db='pearl')
	cur = db.cursor()
	try:
		cur.execute(sql_delete)
		db.commit()
	except Exception as e:
		print "操作异常：%s" %str(e)
		db.rollback()
	finally:
		cur.close()
		db.close()
def update_db(sql_update):
	db=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='123456',db='pearl')
	cur = db.cursor()
	try:
		cur.execute(sql_update)
		db.commit()
	except Exception as e:
		print "操作异常：%s" %str(e)
		db.rollback()
	finally:
		cur.close()
		db.close()

def insert_db(sql_insert):
	db=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='123456',db='pearl')
	cur = db.cursor()
	try:
		cur.execute(sql_insert)
		db.commit()
	except Exception as e:
		print "操作异常：%s" %str(e)
		db.rollback()
	finally:
		cur.close()
		db.close()
if __name__=="__main__":
	sql="select psw from user where name='yo_yo4'"
	a = select_db(sql)[0][0]
	print "查询结果：%s" %a
	sql_delete = "delete from user where name = 'yo_yo1'"
	delete_db(sql_delete)
	sql_update = "update user set psw='666666' where name = 'yo_yo'"
	update_db(sql_update)
	sql_insert = "insert into user(name, psw) values('yoyo_10', '123456')"
	insert_db(sql_insert)