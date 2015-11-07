from fabricasqlcnx import Fabricacnx
__author__ = 'Gabriel Lopes 27/09/15'


class Fabricad(Fabricacnx):
    def __init__(self):
        Fabricacnx.__init__(self)

    def apaga(self, d):
        self.query = d
        Fabricacnx.conector(self)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
