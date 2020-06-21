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
    sql = "SELECT * FROM Student"
    cur.execute(sql)  #执行
    results = cur.fetchall()   #接收
    #循环打印
    for row in results:
        name = row[0]
        email = row[1]
        age = row[2]
        print('Name:%s,Email:%s,Age:%s'%(name,email,age))

except pymysql.Error as e:
    print("数据查询失败！"+str(e))
    db.rollback() #数据库回滚

db.close()