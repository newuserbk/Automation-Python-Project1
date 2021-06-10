"""
This is multiline comment
"""

import pymysql


class DBUtility(object):

    def __init__(self):
        pass

    def create_connection(self):
        connection = pymysql.connect()
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()

    def execute_sql(self, sql):
        pass
