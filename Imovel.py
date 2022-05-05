class Imovel:

    def __init__(self, endereco):
        self.__situacao = "SEM INFO SOBRE SITUACAO"
        self.__tipo = None
        self.__endereco = endereco
        

    def muda_situacao(self, escolha):
        if escolha == 'ALUGADO':
            self.__situacao = 'ALUGADO'
            
        else:
            self.__situacao = 'DISPONIVEL'
        

    def set_situacao_true(self):
        self.__situacao = 'ALUGADO'


    def set_situacao_false(self):
        self.__situacao = 'DISPONIVEL'
 


    def adiciona_endereco(self, endereco):
        self.__endereco = endereco


    def get_situacao(self):
        return self.__situacao


    def set_tipo(self, tipo):
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo

    def get_endereco(self):
        return self.__endereco