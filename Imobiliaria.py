from Cores import Cores

cor = Cores()

class Imobiliaria:

    def __init__(self, nome):
        self.__nome = nome
        self.__lstImoveisAlugar = []

    
    def setNomeImobiliaria(self, nome):
        self.__nome = nome

    def getNomeImobiliaria(self):
        return self.__nome
    
    def adicionaImovel(self, imovel):
        self.__lstImoveisAlugar.append(imovel)
    
    def retornaImovel(self):
        if len (self.__lstImoveisAlugar) > 0:
            print(f"{cor.azul}\nImóveis cadastrados até o momento: ")
            for imovel in self.__lstImoveisAlugar:
                if imovel.getTipo() == 'CASA':
                    print(f"{cor.azul}------------------------------------------------")
                    print (f"{imovel.getEndereco(),  imovel.getTipo(), imovel.getSituacao()}")
                else:
                    print(f"{cor.azul}------------------------------------------------")
                    print (f"{imovel.getEndereco(),  imovel.getTipo(), imovel.getSituacao()}")
        
    
    def validaImovel(self, endereco):
        for imovel in self.__lstImoveisAlugar:
            if imovel.getEndereco() == endereco:
                return True
        return False

    def getListaImovel(self):
        return self.__lstImoveisAlugar


    def validaListaImovel(self):
        if len(self.__lstImoveisAlugar) > 0:
            return True
        return False