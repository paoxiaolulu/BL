#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

#-------step1.数据库配置---------
db_config = {
'host': '47.100.182.135',
'port': 3306,
'db_name': 'tpshop',
'user': 'tpshop',
'passwd': 'tpshop123456',
'charset':'utf8mb4',
'cursorclass':pymysql.cursors.DictCursor
}

#-----step2.初始化数据库测试数据----
# 初始化数据库数据
def setDatabaseAsDefault(DB_NAME):
    conn = pymysql.connect(**db_config)
    conn.autocommit(1)
    cursor = conn.cursor()

    try:
        # 连接数据库
        DB_NAME = 'tpshop'
        conn.select_db(DB_NAME)

        # 删除老用户信息，测新用户测试场景
        count = cursor.execute(
            "select * from tp_users where user_id=47;")
        print(count)

        # 获取表名信息
        desc = cursor.description
        # print "%s %3s" % (desc[0][0], desc[1][0])
        # cursor.scroll(10,mode='absolute')
        results = cursor.fetchall()
        return results
        # for result in results:
        # print result['hardware_num']

    except:
        import traceback
        traceback.print_exc()
        # 发生错误时会滚
        conn.rollback()
    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        conn.close()


