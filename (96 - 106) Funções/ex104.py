"""
Recriar função input() para leitura apenas de int
"""

def leiaint():
    cond = 1
    valor = ""
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    
    while(cond):
        cond = 0
        valor = input("Digite um valor: ")
        if(valor == ""): cond = 1
        
        for i in range (len(valor)):
            if(valor[i] in numbers) == False: cond = 1
            
        if(cond == 1): print("ERRO: Digite um valor inteiro valido")
    return valor

n = leiaint()
print(f"Você acaba de digitar o numero {n}")