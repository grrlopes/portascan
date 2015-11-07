from fabrical import Fabrical
from fabricag import Fabricag
from fabricad import Fabricad
import telnetlib
import socket
import time
__author__ = 'Gabriel Lopes 21/09/15'


class Fabricaproc(Fabrical, Fabricag, Fabricad):
    def __init__(self, debug, fail, log, disco, arquivo):
        Fabrical.__init__(self), Fabricag.__init__(self),
        Fabricad.__init__(self)
        Fabrical.obter(self)
        self.fail = fail
        self.log = log
        self.printa = self.debug = debug
        for i in self.lista:
            proj = i[0]
            ip = i[1]
            i.remove(i[0])
            i.remove(i[0])
            try:
                th = socket.gethostbyaddr(ip)
                uu = {ip: th[0]}
            except socket.error:
                uu = {ip: 'Sem nome'}
            for x in i:
                try:
                    h = telnetlib.Telnet(host=ip, port=x, timeout=0.1)
                    if self.debug == 'sim':
                        print(ip, '=>', x, '- OK')
                    h.close()
                    ipp = proj, uu[ip], ip, x, 'OK', time.strftime('%Y-%m-%d %H:%M:%S')
                    self.resul_ok.append(ipp)
                except socket.error:
                    ippp = proj, uu[ip], ip, x, 'Falha', time.strftime('%Y-%m-%d %H:%M:%S')
                    self.resul_erro.append(ippp)
                    if self.fail == 'sim':
                        print(ip, '=>', x, '- Falha')
                    continue
        #Fabricad.apaga(self, self.trunc)
        #Fabricag.gravaok(self, self.grava_ok)
        #Fabricag.gravafalha(self, self.grava_falha)
        if disco is not None and arquivo is not None:
            Fabricag.logok(self, disco, arquivo)
            Fabricag.valida(self, disco, arquivo)
