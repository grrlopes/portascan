__author__ = 'Gabriel Lopes 23/09/15'


class Fabricaajuda:
    def __init__(self):
        self.ajudaLoca = 'Informe o local do arquivo. Ex: /tmp/lista.txt\nLocal: '
        self.ajudaLocagrava = 'Informe o local onde sera gravado log. Ex: /var/log\nLocal: '
        self.ajudaLocaarch = 'Informe o nome do arquivo. Ex: teste.log\nNome do arquivo de log: '
        self.ajudanoarch = 'Informe um diretorio valido!\nLocal: '
        self.ajudaarch = 'Informe um arquivo!\nArquivo: '
        self.ajudaarchoutro = 'Informe outro arquivo!\nArquivo: '
        self.ajudaachei = 'Arquivo encontrado, deseja sobrescrever ?\nsim ou nao: '
        self.ajudaCampo = 'Campo local vazio\r'
        self.ajudaSepara = 'Informe o tipo do separador. Ex: , - | :\nSeparador: '
        self.ajudaCampoSepara = 'Campo separador vazio'
        self.ajudaDebuga = 'Deseja acompanha os testes em tempo real ?\n' \
                           'Aviso: EM MODO DEBUG APLICACAO NAO EXECUTARA EM BACKGROUND!!!\nsim ou nao: '
        self.ajudaFail = 'Deseja que mostre os testes com falha em tempo real ?\n' \
                         'Aviso: EM MODO DEBUG APLICACAO NAO EXECUTARA EM BACKGROUND!!!\nsim ou nao: '
        self.ajudaDir = '\nNão foi possível localizar o arquivo ou diretório'
        self.ajudaResul = 'Informe o local que será gravado o resultado de Sucesso e Falha.\n ' \
                          'ATENÇÃO: SISTEMA NÃO APAGA OS ARQUIVOS GERADOS\n'
        self.ajudaOk = 'Log de sucesso: '
        self.ajudaFalha = 'Log de falha: '
        self.ajudalog = 'Gravar os logs de falha e sucesso ?\nsim ou nao: '
        self.ajudaselec = 'select * from ip_porta'
        self.ajudatrunc = 'truncate table fabrica'
        self.ajudainserir = ("INSERT INTO fabrica(sistema,host,ip,porta,status,data)"
                             "VALUES (%(sistema)s, %(host)s, %(ip)s, %(porta)s, %(status)s, %(data)s)")
