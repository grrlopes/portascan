from fabricasqlcnx import Fabricacnx
import os
__author__ = 'Gabriel Lopes 22/09/15'


class Fabricag(Fabricacnx):
    def __init__(self):
        Fabricacnx.__init__(self)
        self.resul_ok = []
        self.resul_erro = []
        self.printa = None

    def gravaok(self, grava):
        for i in self.resul_ok:
            self.param = {'sistema': i[0], 'host': i[1],
                          'ip': i[2], 'porta': i[3],
                          'status': i[4], 'data': i[5]}
            if self.printa == 'sim':
                print(self.param)
            self.query = grava
            Fabricacnx.conector(self)
            self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def gravafalha(self, falha):
        for i in self.resul_erro:
            self.param = {'sistema': i[0], 'host': i[1],
                          'ip': i[2], 'porta': i[3],
                          'status': i[4], 'data': i[5]}
            if self.printa == 'sim':
                print(self.param)
            self.query = falha
            Fabricacnx.conector(self)
            self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def logok(self, disco, arquivo):
        arquivo = disco+'/'+arquivo
        print(arquivo)
        for i in self.resul_ok:
            t = 'Sistema: %s Hostname: %s IP: %s ' \
                'Porta: %s Status: %s Data: %s\n' % \
                (i[0], i[1], i[2],
                 i[3], i[4], i[5])
            print(t)
            abrir = open(arquivo, 'a')
            abrir.write(t)
            abrir.close()
        for i in self.resul_erro:
            t = 'Sistema: %s Hostname: %s IP: %s  ' \
                'Porta: %s Status: %s Data: %s\n' % \
                (i[0], i[1], i[2],
                 i[3], i[4], i[5])
            print(t)
            abrir = open(arquivo, 'a')
            abrir.write(t)
            abrir.close()

    @staticmethod
    def valida(disco, arquivo):
        try:
            for dirr in os.listdir((os.path.abspath(disco))):
                if dirr == arquivo:
                    return 'achei'
            return 'nao achei'
        except NotADirectoryError:
            return 'nodir'
        except FileNotFoundError:
            return 'nofile'
        except IsADirectoryError:
            return 'errodir'

    @staticmethod
    def validarq(disco, arquivo):
        valida = disco+'/'+arquivo
        if os.path.isdir(valida):
            return 'sim'
        else:
            return 'nao'

    @staticmethod
    def validadir(disco):
        if os.path.isdir(disco):
            return 'sim'
        else:
            return 'nao'
