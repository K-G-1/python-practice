#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", " ", "test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
# select 查询
sql = "SELECT * FROM kg_date "
try:
  # 执行SQL语句
  cursor.execute(sql)
  # 获取所有记录列表
  results = cursor.fetchall()
  for row in results:
    name = row[0]
    age = row[1]
    sex =row[2]
    income = row[3]
    # 打印结果
    print "name=%s,age=%d,sex=%s,income=%d" % \
        (name, age, sex, income)
except:
  print "Error: unable to fecth data"

# 关闭数据库连接
db.close()
