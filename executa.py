#!/usr/bin/env python3
import time
import csv
import sys
import mysql.connector
from fabricaproc import Fabricaproc, Fabrical, Fabricag
__author__ = 'Gabriel Lopes 19/09/15'


class Executa(Fabrical, Fabricag):
    def __init__(self):
        Fabrical.__init__(self)
        while True:
            sys.stdout.write(self.ajudaDebuga)
            self.debug = str(input())
            if self.debug == 'sim' or self.debug == 'nao':
                break
        self.fail = 'nao'
        if self.debug == 'sim':
            while True:
                sys.stdout.write(self.ajudaFail)
                self.fail = str(input())
                if self.fail == 'sim' or self.fail == 'nao':
                    break
        while True:
            sys.stdout.write(self.ajudalog)
            self.gravalog = str(input())
            if self.gravalog == 'sim' or self.gravalog == 'nao':
                break
        self.disco = None
        self.arch = None
        self.noarch = None
        if self.gravalog == 'sim':
            while True:
                if self.noarch is None:
                    sys.stdout.write(self.ajudaLocagrava)
                self.disco = str(input())
                self.noarch = Fabricag.validadir(self, self.disco)
                if self.noarch == 'nao':
                    sys.stdout.write(self.ajudanoarch)
                if self.disco is not '' and self.noarch == 'sim':
                    break
            self.valor = None
            self.entravalor = None
            while True:
                if self.arch is None:
                    sys.stdout.write(self.ajudaLocaarch)
                self.arch = str(input())
                self.valor = Fabricag.valida(self.disco, self.arch)
                if self.valor == 'achei':
                    while True:
                        if self.valor == 'achei' and self.entravalor is None:
                            sys.stdout.write(self.ajudaachei)
                            self.achei = str(input())
                            if self.achei == 'nao':
                                self.valor1 = None
                                while True:
                                    if self.valor1 is None:
                                        sys.stdout.write(self.ajudaarch)
                                    else:
                                        sys.stdout.write(self.ajudaarchoutro)
                                    self.arch = str(input())
                                    self.valor1 = Fabricag.valida(self.disco, self.arch)
                                    if self.valor1 == 'nao achei':
                                        break
                        elif self.achei == 'sim':
                            break
                if self.valor == 'nao achei':
                    break
                elif self.entravalor == 'sim':
                    break
        while True:
            '''Fabricaproc(self.debug, self.fail,
                        self.gravalog, self.disco,
                        self.arch)'''
            print('kkkk')
            time.sleep(5)


class Principal:
    if __name__ == "__main__":
        Executa()


def gabriel():
    with open('/tmp/BaselineIndra.csv', 'r') as f:
        ler = csv.reader(f, delimiter=',')
        for linha in ler:
            syss = linha[0]
            ip = linha[1]
            linha.remove(linha[0])
            linha.remove(linha[0])
            for eu in linha:
                print('Sistema: ', syss, '<===>  IP: ', ip, '<===>  PORTA: ', eu)


def negraoo():
    cnx = mysql.connector.connect(user='fabrica', password='@fabr1ca', host='10.130.214.27', database='fabricateste')
    cursor = cnx.cursor()
    '''
    query = 'select * from ip_porta'
    cursor.execute(query)
    for i in cursor:
        v = i[1].decode()+','+i[2].decode()
        vv = v
        vvv = i[3].decode()
        gg = [vv+','+vvv]
        l = csv.reader(gg, delimiter=',')
        for k in l:
            ip = k[1]
            k.remove(k[0])
            k.remove(k[0])
            for j in k:
                print('ip :', ip, 'porta :', j)
    '''
    with open('/tmp/BaselineIndra3.csv', 'r') as f:
        ler = csv.reader(f, delimiter=',')
        for linha in ler:
            syss = linha[0]
            ip = linha[1]
            linha.remove(linha[0])
            linha.remove(linha[0])
            for eu in linha:
                colher = {'sistema': syss, 'ip': ip, 'porta': eu}
                inserir = "insert into ip_porta(sistema,ip,porta)VALUES(%(sistema)s, %(ip)s, %(porta)s)"
                cursor.execute(inserir, colher)
                print('Sistema: ', syss, 'IP: ', ip, 'POrTA: ', eu)
    cnx.commit()
    cursor.close()
    cnx.close()
'''
    tt = i[1].decode()+','+i[2].decode()
    t = tt
    euu = i[3].decode()
    gg = [t+','+euu]
    print(gg)
    l = csv.reader(gg, delimiter=',')
    for k in l:
        ip = k[1]
        k.remove(k[0])
        k.remove(k[0])
        for j in k:
            print('ip :', ip, 'porta :', j)
'''
