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
    cur.execute("DROP TABLE IF EXISTS Student")
    sql = "CREATE TABLE Student(Name CHAR(20) NOT NULL, Email CHAR(20), Age INT)"
    cur.execute(sql)
    print("表格创建成功！")
except pymysql.Error as e:
    print("表格创建失败！"+str(e))
