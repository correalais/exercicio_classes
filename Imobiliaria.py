from Cores import Cores

cor = Cores()

class Imobiliaria:

    def __init__(self, nome):
        self.__nome = nome
        self.__lst_imoveis_alugar = []

    
    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def adiciona_imovel(self, imovel):
        self.__lst_imoveis_alugar.append(imovel)
    
    def retorna_imovel(self):
        if len (self.__lst_imoveis_alugar) > 0:
            print(f"{cor.azul}\nImóveis cadastrados até o momento: ")
            for imovel in self.__lst_imoveis_alugar:
                if imovel.get_tipo() == 'CASA':
                    print(f"{cor.azul}------------------------------------------------")
                    print (f"{imovel.get_endereco(),  imovel.get_tipo(), imovel.get_situacao()}")
                else:
                    print(f"{cor.azul}------------------------------------------------")
                    print (f"{imovel.get_endereco(),  imovel.get_tipo(), imovel.get_situacao()}")
        
    
    def valida_imovel(self, endereco):
        for imovel in self.__lst_imoveis_alugar:
            if imovel.get_endereco() == endereco:
                return True
        return False

    def get_lista_imovel(self):
        return self.__lst_imoveis_alugar


    def valida_lista(self):
        if len(self.__lst_imoveis_alugar) > 0:
            return True
        return False