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
    sql = "INSERT INTO Student(Name,Email,Age) VALUE (%s,%s,%s)"
    value = ('Mike','123@163.com',20)
    cur.execute(sql,value)  #执行
    db.commit()   #提交数据库
    print("数据插入成功！")
except pymysql.Error as e:
    print("数据插入失败！"+str(e))
    db.rollback() #数据库回滚

db.close()