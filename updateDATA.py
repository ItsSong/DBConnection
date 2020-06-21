#!/usr/bin/env python
#-*- coding = utf-8 -*-
import pymysql

DBhost = 'localhost'
DBuser = 'root'
DBpass = 'songzhuo0813-+'
DBname = 'test'

try:
    db = pymysql.connect(DBhost,DBuser,DBpass,DBname)
    print("数据库连接成功！")
    cur = db.cursor()  #声明一个游标
    sql = "update Student set NAME=%s where NAME=%s"
    value = ('John','Mike')
    cur.execute(sql,value)  #执行
    db.commit()
    print('更新成功！')

except pymysql.Error as e:
    print("数据更新失败！"+str(e))
    db.rollback() #数据库回滚

db.close()