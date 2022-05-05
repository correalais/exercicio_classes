
lst_imobiliarias = []

class Cores: 
    azul = '\033[94m'
    verde = '\033[92m'
    amarelo = '\033[93m'
    rosa = '\033[95m'
    vermelho = '\033[91m'
    branco = '\033[0;37m'

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

    #def set_telefone(self,telefone):
        #self.__telefones.append(telefone)
    
    #def get_telefone(self):
        #if len(self.__telefones) > 0:
            #return self.__telefones

    def get_lista_imovel(self):
        return self.__lst_imoveis_alugar


    def valida_lista(self):
        if len(self.__lst_imoveis_alugar) > 0:
            return True
        return False



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




################################################################


def relatorio_imobiliarias():
    if len (lst_imobiliarias) > 0:
        mostra_imobiliaria()
        relatorio_imoveis()    
    else:
        print(f"\n{cor.vermelho}Ainda não existem imobiliarias cadastradas")

def relatorio_imoveis():
    if len(lst_imobiliarias) > 0:
        nome = input(f"\n{cor.amarelo}Digite o nome da imobiliária para listar os imóveis: ").upper()
        if valida_imobiliaria(nome) == True:
            for imobiliaria in lst_imobiliarias:
                if imobiliaria.get_nome() == nome:
                    if len(imobiliaria.get_lista_imovel()) > 0:
                        imobiliaria.retorna_imovel()
                        
                    else:
                        print (f"{cor.vermelho}\nA imobiliária ainda não possui imóveis cadastrados!")
        else:
            print(f"{cor.vermelho}\nNenhuma imobiliária com este nome está na lista!")         
                    
    else:
        print (f"{cor.vermelho}\nNenhum imóvel foi cadastrado ainda!")

def mostra_imobiliaria():
    if len (lst_imobiliarias) > 0:
        print(f"\n{cor.amarelo}Imobiliárias cadastradas até o momento:")
        for imobiliaria in lst_imobiliarias:
            print(f"\n{imobiliaria.get_nome()}")


def valida_imobiliaria(nome):
    for imobiliaria in lst_imobiliarias:
        if imobiliaria.get_nome() == nome:
            return True        
    return False


"""def adiciona_numero(nome_imobiliaria):
    while True:
        try:
            numero = int(input(f"{cor.amarelo}\nDigite um numero para a imobiliaria: "))
            for imobiliaria in lst_imobiliarias:
                if valida_imobiliaria(nome_imobiliaria) == True:
                    if imobiliaria.get_nome() == nome_imobiliaria:
                        imobiliaria.set_telefone(numero)
            novamente = input(f"{cor.amarelo}\nDeseja adicionar mais um número? S para sim, N para não: ").upper()
            if novamente == 'N':
                break
        except:
            print(f"{cor.vermelho}\nDigite números!")
"""


    
    

            
def cadastrar_imobiliaria():
    mostra_imobiliaria()
    nome_imobiliaria = input(f"\n{cor.amarelo}Digite o nome da Imobiliária para cadastrar: ").upper()
    if valida_imobiliaria(nome_imobiliaria) == False:
        imobiliaria = Imobiliaria(nome_imobiliaria)
        lst_imobiliarias.append(imobiliaria)
        #adiciona_numero(nome_imobiliaria)        
        print(f"{cor.verde}\nCadastro de imobiliaria concluído.")
    else:
        escolha =  input(f"{cor.vermelho}\nEsta imobiliária já está na lista. Deseja adicionar outra? S para sim, N para não: ").upper()
        if escolha == 'S':
            cadastrar_imobiliaria() 
            
        else:
            print (f"{cor.verde}\nOk, encerramos.") 




def cadastrar_imovel():
    mostra_imobiliaria()
    if len (lst_imobiliarias) > 0:
        nome_imobiliaria =  input(f"\n{cor.amarelo}Digite o nome da Imobiliária ao qual o imóvel pertence: ").upper()
        for imobiliaria in lst_imobiliarias:
            if valida_imobiliaria(nome_imobiliaria) == True:
                if imobiliaria.get_nome() == nome_imobiliaria:
                    if imobiliaria.retorna_imovel() != False:
                        endereco_imovel = input(f"\n{cor.amarelo}Digite o endereco completo do imóvel (com endereco e número separados por vírgula sem espaços): ").upper()             
                        if imobiliaria.valida_imovel(endereco_imovel) == False:
                            imovel = Imovel(endereco_imovel)
                            tipo_imovel = input(f"\n{cor.amarelo}Digite o tipo do imóvel (casa ou apartamento somente): ").upper()
                            if tipo_imovel == 'CASA': 
                                imovel.set_tipo(tipo_imovel)
                                imobiliaria.adiciona_imovel(imovel)
                                
                            elif tipo_imovel == 'APARTAMENTO':
                                imovel.set_tipo(tipo_imovel)
                                imobiliaria.adiciona_imovel(imovel)
                               
                            else:
                                escolha = input(f"\n{cor.vermelho}Você só pode adicionar casas e apartamentos! Deseja tentar novamente? S para sim, N para não: ").upper()
                                if escolha == 'S':
                                    cadastrar_imovel()
                                    break
                                else:
                                    print (f"{cor.verde}\nEncerramos.")
                                    break
                            situacao = input(f"\n{cor.amarelo}Digite a situação do imóvel: 1 para alugado, 2 para disponível: ")
                            if situacao == '1':
                                    imovel.set_situacao_true() 
                                    print(f"{cor.verde}\nCadastro concluído.") 
                                    break                                   
                            else:
                                imovel.set_situacao_false()  
                                print(f"{cor.verde}\nCadastro concluído.") 
                                break
                            
                        else:
                            escolha = input(f"\n{cor.vermelho}Imóvel já cadastrado. Deseja adicionar um novo? S para sim, N para não: ").upper()
                            if escolha == 'S':
                                cadastrar_imovel()
                                
                            else:
                                print (f"{cor.verde}\nEncerramos.")

            else:
                escolher = input (f"{cor.vermelho}\nImobiliaria ainda não está na lista. Deseja adicionar? S para Sim, N para não: ").upper()
                if escolher == 'S':
                    cadastrar_imobiliaria()
                    cadastrar_imovel()
                    

                else:
                    print (f"{cor.verde}\nEncerramos.")
                    break
                    
    else:
        print (f"{cor.vermelho}\nNão há imobiliarias cadastradas ainda")

def atualiza_status():
    if len(lst_imobiliarias) > 0:
        mostra_imobiliaria()
        nome_imobiliaria = input(f"\n{cor.amarelo}Digite o nome da imobiliária para buscar o imóvel: ").upper()
        if valida_imobiliaria(nome_imobiliaria) == True:
            for imobiliaria in lst_imobiliarias:
                if imobiliaria.get_nome() == nome_imobiliaria:
                    if imobiliaria.valida_lista() == True:
                        imobiliaria.retorna_imovel()
                        endereco_imovel = input(f"\n{cor.amarelo}Digite o endereco completo do imóvel para alterar o status (com endereço e número separados por vírgula sem espaços): ").upper()
                        if imobiliaria.valida_imovel(endereco_imovel) == True:
                            for imovel in imobiliaria.get_lista_imovel():
                                if imovel.get_endereco() == endereco_imovel:
                                        escolha = input(f"\n{cor.amarelo}Escolha: 1 para alugado, 2 para disponível: ").upper()
                                        if escolha == '1':
                                            imovel.set_situacao_true()
                                            print(f"\n{cor.verde}Concluído")
                                            break
                                        elif escolha == '2':
                                            imovel.set_situacao_false()
                                            print(f"\n{cor.verde}Concluído")
                                            break
                                        else:
                                            print(f"\n{cor.vermelho}Escolha algo válido!")
                        else:
                            print(f"\n{cor.vermelho}Nenhum imóvel encontrado.")
                    else:
                        print(f"\n{cor.vermelho}A imobiliária ainda não possui nenhum imóvel cadastrado.")


        else:
            print(f"\n{cor.vermelho}Não há nenhuma imobiliária com esse nome na lista.")
    else:
        print(f"\n{cor.vermelho}Ainda não foram cadastradas imobiliárias.")




def inicializar():
    arquivo = open("imobiliarias.txt", "r")
    try:
        for linha in arquivo:
            lista = linha.strip().split(";")
            nome_imobiliaria = lista[0]
            if valida_imobiliaria(nome_imobiliaria) == False:
                imobiliaria = Imobiliaria(nome_imobiliaria)
                #imobiliaria.seta_telefone((lista[1])) 
                lst_imobiliarias.append(imobiliaria)

            for imobiliaria in lst_imobiliarias:
                if valida_imobiliaria(nome_imobiliaria) == True:
                    if imobiliaria.get_nome() == nome_imobiliaria:
                        endereco_imovel = lista[2]
                        if imobiliaria.valida_imovel(endereco_imovel) == False:
                            imovel = Imovel(endereco_imovel)
                            imovel.muda_situacao(lista[3])
                            imovel.set_tipo(lista[1])                                                    
                            imobiliaria.adiciona_imovel(imovel)   
    finally:
        arquivo.close



def finalizar():
    arquivo = open("imobiliarias.txt", "r+")     
    for imobiliaria in lst_imobiliarias:            
        for imovel in imobiliaria.get_lista_imovel():    
            arquivo.write(imobiliaria.get_nome()+ ";"+ imovel.get_tipo()+";"+imovel.get_endereco()+";"+imovel.get_situacao()+"\n")

    arquivo.close
                          
def menu_principal():
    print( f"""\n\n {cor.rosa}                    Bem - vindo ao menu!   
                    ----------------------------------
                    0. Encerrar Programa
                    1. Adionar Imobiliaria
                    2. Adicionar Imóvel
                    3. Relatório de Imobiliárias e seus imóveis
                    4. Alterar status Alugado/Disponível                   
                    ----------------------------------
                    """)

def escolhas():
    
    escolha = input (f"{cor.rosa}Digite a opção que deseja: """)
    if escolha == '1':
        cadastrar_imobiliaria()
    elif escolha == '2':
        cadastrar_imovel()
    elif escolha == '3':
        relatorio_imobiliarias()
    elif escolha =='4':
        atualiza_status()
    elif escolha =='0':
        print(f"{cor.verde}\nVocê escolheu encerrar.") 
        return False      
    else:
        print (f"{cor.vermelho}\nEscolha uma opção válida!")



inicializar()

while True:

    menu_principal()
    if escolhas() == False:  
        break

finalizar()