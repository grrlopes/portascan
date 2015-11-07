from fabricaajuda import Fabricaajuda
from fabricasqlcnx import Fabricacnx
import csv
import sys
__author__ = 'Gabriel Lopes 25/09/15'


class Fabrical(Fabricaajuda, Fabricacnx):
    def __init__(self):
        Fabricaajuda.__init__(self), Fabricacnx.__init__(self)
        self.local = '/tmp/sistemavivo.txt'
        self.separa = ','
        self.grava_ok = self.ajudainserir
        self.grava_falha = self.ajudainserir
        self.trunc = self.ajudatrunc
        self.lista = []
        self.msg = None
        self.direrror = None

    def ler(self):
        try:
            with open(self.local, 'r') as local:
                ler = csv.reader(local, delimiter=self.separa)
                for l in ler:
                    self.lista.append(l)
        except FileNotFoundError:
            print(self.ajudaDir)
        except IsADirectoryError:
            print(self.ajudaDir)

    def obter(self):
        self.negrao()
        try:
            for i in self.lista:
                self.msg = i[1]
        except IndexError:
            print('\n Linhas separadas por', '"', self.separa, '"'
                  'fora do padrão... verifique!!!')
            sys.exit()

    def negrao(self):
        self.query = self.ajudaselec
        Fabricacnx.conector(self)
        for i in self.cursor:
            v = i[1].decode()+','+i[2].decode()
            vv = v
            vvv = i[3].decode()
            l = [vv+','+vvv]
            ler = csv.reader(l, delimiter=self.separa)
            for x in ler:
                self.lista.append(x)
        self.cursor.close()
        self.conn.close()