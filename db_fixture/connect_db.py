# -*- coding: utf-8 -*-
import MySQLdb.cursors
import json

class OperationMysql:
    def __init__(self):
        conn = MySQLdb.connect(
            host='localhost',
            post=8080,
            user='root',
            passwd='123456',
            db='lell',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )
        self.cur = conn.cursor()

    #查询一条数据
    def serch(self,sql):
        self.cur.execute(sql)
        res = self.cur.fetchone()
        return json.dumps(res)


if __name__ == '__main__':
    op_mysql = OperationMysql()
    op_mysql.serch("select * from test")