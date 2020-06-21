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
except pymysql.Error as e:
    print("数据库连接失败！"+str(e))
