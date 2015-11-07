import mysql
__author__ = 'Gabriel Lopes 26/09/15'


class Fabricacnx:
    def __init__(self):
        self.ip = '192.xxxxxx'
        self.bd = 'fabricateste'
        self.user = 'xxxxx'
        self.senha = '123456'
        self.conn = None
        self.cursor = None
        self.query = None
        self.param = None

    def conector(self):
        self.conn = mysql.connector.connect(user=self.user, password=self.senha, host=self.ip, database=self.bd)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.param)
