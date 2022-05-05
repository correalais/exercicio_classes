from Imobiliaria import Imobiliaria
from Imovel import Imovel
from Cores import Cores

cor = Cores()

lstImobiliarias = []

def relatorioImobiliarias():
    if len (lstImobiliarias) > 0:
        imprimeImobiliaria()
        relatorioImoveis()    
    else:
        print(f"\n{cor.vermelho}Ainda não existem imobiliarias cadastradas")

def relatorioImoveis():
    if len(lstImobiliarias) > 0:
        nome = input(f"\n{cor.amarelo}Digite o nome da imobiliária para listar os imóveis: ").upper()
        if validaImobiliaria(nome) == True:
            for imobiliaria in lstImobiliarias:
                if imobiliaria.getNomeImobiliaria() == nome:
                    if len(imobiliaria.getListaImovel()) > 0:
                        imobiliaria.retornaImovel()
                        
                    else:
                        print (f"{cor.vermelho}\nA imobiliária ainda não possui imóveis cadastrados!")
        else:
            print(f"{cor.vermelho}\nNenhuma imobiliária com este nome está na lista!")         
                    
    else:
        print (f"{cor.vermelho}\nNenhum imóvel foi cadastrado ainda!")

def imprimeImobiliaria():
    if len (lstImobiliarias) > 0:
        print(f"\n{cor.amarelo}Imobiliárias cadastradas até o momento:")
        for imobiliaria in lstImobiliarias:
            print(f"\n{imobiliaria.getNomeImobiliaria()}")


def validaImobiliaria(nome):
    for imobiliaria in lstImobiliarias:
        if imobiliaria.getNomeImobiliaria() == nome:
            return True        
    return False


            
def cadastraImobiliaria():
    imprimeImobiliaria()
    nomeImobiliaria = input(f"\n{cor.amarelo}Digite o nome da Imobiliária para cadastrar: ").upper()
    if validaImobiliaria(nomeImobiliaria) == False:
        imobiliaria = Imobiliaria(nomeImobiliaria)
        lstImobiliarias.append(imobiliaria)   
        print(f"{cor.verde}\nCadastro de imobiliaria concluído.")
    else:
        escolha =  input(f"{cor.vermelho}\nEsta imobiliária já está na lista. Deseja adicionar outra? S para sim, N para não: ").upper()
        if escolha == 'S':
            cadastraImobiliaria() 
            
        else:
            print (f"{cor.verde}\nOk, encerramos.") 




def cadastraImovel():
    imprimeImobiliaria()
    if len (lstImobiliarias) > 0:
        nomeImobiliaria =  input(f"\n{cor.amarelo}Digite o nome da Imobiliária ao qual o imóvel pertence: ").upper()
        for imobiliaria in lstImobiliarias:
            if validaImobiliaria(nomeImobiliaria) == True:
                if imobiliaria.getNomeImobiliaria() == nomeImobiliaria:
                    if imobiliaria.retornaImovel() != False:
                        enderecoImovel = input(f"\n{cor.amarelo}Digite o endereco completo do imóvel (com endereco e número separados por vírgula sem espaços): ").upper()             
                        if imobiliaria.valida_imovel(enderecoImovel) == False:
                            imovel = Imovel(enderecoImovel)
                            tipoImovel = input(f"\n{cor.amarelo}Digite o tipo do imóvel (casa ou apartamento somente): ").upper()
                            if tipoImovel == 'CASA': 
                                imovel.setTipo(tipoImovel)
                                imobiliaria.adicionaImovel(imovel)
                                
                            elif tipoImovel == 'APARTAMENTO':
                                imovel.setTipo(tipoImovel)
                                imobiliaria.adicionaImovel(imovel)
                               
                            else:
                                escolha = input(f"\n{cor.vermelho}Você só pode adicionar casas e apartamentos! Deseja tentar novamente? S para sim, N para não: ").upper()
                                if escolha == 'S':
                                    cadastraImovel()
                                    break
                                else:
                                    print (f"{cor.verde}\nEncerramos.")
                                    break
                            situacao = input(f"\n{cor.amarelo}Digite a situação do imóvel: 1 para alugado, 2 para disponível: ")
                            if situacao == '1':
                                    imovel.setSituacaoTrue() 
                                    print(f"{cor.verde}\nCadastro concluído.") 
                                    break                                   
                            else:
                                imovel.setSituacaoFalse()  
                                print(f"{cor.verde}\nCadastro concluído.") 
                                break
                            
                        else:
                            escolha = input(f"\n{cor.vermelho}Imóvel já cadastrado. Deseja adicionar um novo? S para sim, N para não: ").upper()
                            if escolha == 'S':
                                cadastraImovel()
                                
                            else:
                                print (f"{cor.verde}\nEncerramos.")

            else:
                escolher = input (f"{cor.vermelho}\nImobiliaria ainda não está na lista. Deseja adicionar? S para Sim, N para não: ").upper()
                if escolher == 'S':
                    cadastraImobiliaria()
                    cadastraImovel()
                    

                else:
                    print (f"{cor.verde}\nEncerramos.")
                    break
                    
    else:
        print (f"{cor.vermelho}\nNão há imobiliarias cadastradas ainda")

def atualizaStatusImovel():
    if len(lstImobiliarias) > 0:
        imprimeImobiliaria()
        nomeImobiliaria = input(f"\n{cor.amarelo}Digite o nome da imobiliária para buscar o imóvel: ").upper()
        if validaImobiliaria(nomeImobiliaria) == True:
            for imobiliaria in lstImobiliarias:
                if imobiliaria.getNomeImobiliaria() == nomeImobiliaria:
                    if imobiliaria.validaLista() == True:
                        imobiliaria.retornaImovel()
                        enderecoImovel = input(f"\n{cor.amarelo}Digite o endereco completo do imóvel para alterar o status (com endereço e número separados por vírgula sem espaços): ").upper()
                        if imobiliaria.validaImovel(enderecoImovel) == True:
                            for imovel in imobiliaria.getListaImovel():
                                if imovel.getEndereco() == enderecoImovel:
                                        escolha = input(f"\n{cor.amarelo}Escolha: 1 para alugado, 2 para disponível: ").upper()
                                        if escolha == '1':
                                            imovel.setSituacaoTrue()
                                            print(f"\n{cor.verde}Concluído")
                                            break
                                        elif escolha == '2':
                                            imovel.setSituacaoFalse()
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




def inicializaArquivo():
    arquivo = open("imobiliarias.txt", "r")
    try:
        for linha in arquivo:
            lista = linha.strip().split(";")
            nomeImobiliaria = lista[0]
            if validaImobiliaria(nomeImobiliaria) == False:
                imobiliaria = Imobiliaria(nomeImobiliaria)
                lstImobiliarias.append(imobiliaria)

            for imobiliaria in lstImobiliarias:
                if validaImobiliaria(nomeImobiliaria) == True:
                    if imobiliaria.getNomeImobiliaria() == nomeImobiliaria:
                        enderecoImovel = lista[2]
                        if imobiliaria.validaImovel(enderecoImovel) == False:
                            imovel = Imovel(enderecoImovel)
                            imovel.mudaSituacao(lista[3])
                            imovel.setTipo(lista[1])                                                    
                            imobiliaria.adicionaImovel(imovel)   
    finally:
        arquivo.close



def finalizaArquivo():
    arquivo = open("imobiliarias.txt", "r+")     
    for imobiliaria in lstImobiliarias:            
        for imovel in imobiliaria.getListaImovel():    
            arquivo.write(imobiliaria.getNomeImobiliaria()+ ";"+ imovel.getTipo()+";"+imovel.getEndereco()+";"+imovel.getSituacao()+"\n")

    arquivo.close
                          
def menuPrincipal():
    print( f"""\n\n {cor.rosa}                    Bem - vindo ao menu!   
                    ----------------------------------
                    0. Encerrar Programa
                    1. Adionar Imobiliaria
                    2. Adicionar Imóvel
                    3. Relatório de Imobiliárias e seus imóveis
                    4. Alterar status Alugado/Disponível                   
                    ----------------------------------
                    """)

def escolhasMenu():
    
    escolha = input (f"{cor.rosa}Digite a opção que deseja: """)
    if escolha == '1':
        cadastraImobiliaria()
    elif escolha == '2':
        cadastraImovel()
    elif escolha == '3':
        relatorioImobiliarias()
    elif escolha =='4':
        atualizaStatusImovel()
    elif escolha =='0':
        print(f"{cor.verde}\nVocê escolheu encerrar.") 
        return False      
    else:
        print (f"{cor.vermelho}\nEscolha uma opção válida!")



inicializaArquivo()

while True:

    menuPrincipal()
    if escolhasMenu() == False:  
        break

finalizaArquivo()