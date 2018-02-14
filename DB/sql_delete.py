#!/usr/bin/python3
# coding=UTF-8
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", " ", "test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 删除语句
# 1: delete from ex_stu where
# 2:delete from ex_stu limit 3 :删除前3个 (有时配合order by 来使用）
# 
# drop 删除数据库或者数据表
sql = "DELETE FROM employee WHERE AGE > '%d'" % (20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()
