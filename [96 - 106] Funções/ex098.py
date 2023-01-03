"""
Função contador() que recebe 3 parametros: inicio, fim, passo
Realizará 3 cibtagebs através da função criada:
1. 1 até 10 de 1 em 1 
2. 10 até 0 de 2 em 2
3. personalizada
"""

def contador(inicio, fim, passo):

    if passo == 0: passo = 1
    print("Contando: ",end='')
    for i in range(inicio,fim,passo):
        print(f"{i} ",end='')
    print()
        
    
contador(1,11,1)
contador(10,-1,-2)
contador(int(input("Início: ")),int(input("Fim: ")),int(input("Passo: ")))