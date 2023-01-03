"""
Lê nome, idade, sexo de 4 pessoas e motra
- media das idades
- homem mais velho
- quantas mulheres tem menos de 20 anos
"""

somaId = 0
maisVelho = -1
nome = ""
quant = 0

for i in range (4):
    n = input("Nome: ")
    s = input("Sexo: ")
    i = int(input("Idade: "))
    
    somaId+=i
    
    if s == "H" and i > maisVelho:
        maisVelho = i
        nome = n
        
    if s == "M" and i < 20:
        quant+=1
        
print("Média: {}\nHomem: {}\nQuantidade de mulheres: {}".format(somaId/4,nome,quant))
