class Imovel:

    def __init__(self, endereco):
        self.__situacao = "SEM INFO SOBRE SITUACAO"
        self.__tipo = None
        self.__endereco = endereco
        

    def mudaSituacaoImovel(self, escolha):
        if escolha == 'ALUGADO':
            self.__situacao = 'ALUGADO'
            
        else:
            self.__situacao = 'DISPONIVEL'
        

    def setSituacaoTrue(self):
        self.__situacao = 'ALUGADO'


    def setSituacaoFalse(self):
        self.__situacao = 'DISPONIVEL'
 


    def adicionaEndereco(self, endereco):
        self.__endereco = endereco


    def getSituacao(self):
        return self.__situacao


    def setTipo(self, tipo):
        self.__tipo = tipo
        
    def getTipo(self):
        return self.__tipo

    def getEndereco(self):
        return self.__endereco