#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

connect = sqlite3.connect('test.db')
cursor = connect.cursor()
cursor.execute('CREATE TABLE user(id VARCHAR(20) PRIMARY KEY,name VARCHAR(20))')
cursor.execute('INSERT INTO user(id,name) VALUES (\'1\',\'Michael\')')
# 通过rowcount获得插入的行数
print('rowcount=',cursor.rowcount)
cursor.close()
# 提交事务
connect.commit()
connect.close()

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM user WHERE id=?', '1')
# 获得查询结果集
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()