from flask import *
import pymysql



def select_wordinfo_by_word(word):
    # 获取数据库连接
    conn = pymysql.connect(host='127.0.0.1', user='root', password="123456", database='word', port=3306, charset='utf8')
    # 准备一个sql语句
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from word_info where word='" + word + "'"
    # 执行sql语句
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    # 关闭连接 释放资源
    cursor.close()
    conn.close()
    return data


def select(sql):
    # 获取数据库连接
    conn = pymysql.connect(host='127.0.0.1', user='root', password="123456", database='word', port=3306, charset='utf8')
    # 准备一个sql语句
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'select * from word_info'
    # 执行sql语句
    cursor.execute(sql)
    data = cursor.fetchall()
    print("数据库执行结果")
    print(data)
    # 关闭连接 释放资源
    cursor.close()
    conn.close()

