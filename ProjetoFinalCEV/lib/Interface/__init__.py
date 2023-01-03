from lib.parser import *
from time import sleep

def linha(tam=42):
    return tam * "-"

def cabeçalho(txt):
    print(linha())
    print(txt.center(len(linha())))
    print((linha()))

def leiaInt(msg):
    while(True):
        try:
            i = int(input(msg))
        except (ValueError,TypeError):
            print("\033[31mERRO: digite um inteiro valido\n\033[m")
        except KeyboardInterrupt:
            print("\nFechando a aplicação.")
            exit()
        else:
            return i

def showMenu():
    cabeçalho("MENU PRINCIPAL")
    options = ["Ver Pessoas Cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"]
    for i in range(len(options)):
        print(f"\033[33m{i+1}\033[m - \033[34m{options[i]}\033[m")
    print(linha())
             
def mostraPessoas(path):
    cabeçalho("PESSOAS CADASRTADAS")
    dados = lerArquivo(path)
    
    try:
        for dado in dados:
            if(dado != []): 
                dado[1] = str(dado[1]).replace('\n','')
                print(f"Nome: {dado[0]:<18} Idade: {dado[1]:>3} anos")
    except (IndexError,TypeError):
        print("Ainda não foram adicionados dados.")
    
    sleep(1)

def novaPessoa(path):
    cabeçalho("NOVO CADASTRO")
    nome = str(input("Nome: "))
    idade = leiaInt("Idade: ")
    cadastrar(path, nome, idade)

def menu():
    
    path = "dados/teste.txt"
    
    while True:
        showMenu()
        escolha = leiaInt("Escolha uma ação: ")

        match escolha:
            case 1: mostraPessoas(path)
            case 2: novaPessoa(path)
            case 3: 
                print("Saindo do Sistema.")
                exit()
            case _: 
                print("\033[31mERRO: digite um valor valido\n\033[m")
                sleep(1)

