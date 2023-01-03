from lib.Interface import *

def arquivoExiste(path):
    try:
        open(path,'rt')
    except FileNotFoundError: return False
    else: return True
    
def criarArquivo(path):
    try:
        a = open(path,'wt+')
        a.close()
    except:
        print("ERRO na criação do arquivo")
        
def lerArquivo(path):
    try:
        file = open(path, 'rt')
    except:
        print("Erro na leitura do arquivo")
    else:
        dados = [[]]
        for linha in file:
            dado = linha.split(';')
            # print(f"Dado {dado}")
            # print(len(dado))
            # print(f"Dados {dados}")
            # print(len(dados))
            if(dado[0] != "\n"):
                dados.append(dado)
            # print(f"Dados {dados}")
            
        if(len(dados) > 1): 
            return dados
            
    finally:
        file.close()
    
def cadastrar(path, nome, idade):
    try:
        file = open(path, 'at')
    except:
        print("ERRO na abertura do arquivo")
    else:
        try:
            file.write(f"{nome};{idade}\n")
        except:
            print("ERRO na escrita dos arquivos")