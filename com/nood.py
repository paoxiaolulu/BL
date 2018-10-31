#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 数据准备调用mysql

import pymysql
import pymysql.cursors

# ---测试体验版环境：
DB = pymysql.connect(host='47.100.182.135',
                         user='tpshop',
                         password='tpshop123456',
                         db='tpshop',
                         port=3306
                         )

# 使用cursor()方法获取操作游标
cursor = DB.cursor()

# 数据初始化  新用户测试场景使用
sql = "DELETE FROM tp_users where user_id = '%d'" % (47)     # 只需要修改后面的user_id即可
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   DB.commit()
except:
   # 发生错误时回滚
   DB.rollback()

# 关闭数据库
DB.close()