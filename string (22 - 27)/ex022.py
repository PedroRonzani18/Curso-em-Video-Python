""" 
Crie um programa que leira o nome completo de uma pessoa e mostre:
1. O nome com todas as letras maiusculas
2. O nome com todas as letras minusculas
3. Quantas letras ao todo, desconsiderando espaços
4. Quantas letras tem o primeiro nome
"""

nome = input("Digite o nome completo: ")
print("Nome maiusculo: {}".format(nome.upper()))
print("Nome minusculo: {}".format(nome.lower()))
nomes = nome.split(" ")

quant = 0
for i in nome:
    if i != " ":
        quant+=1
        
#quant = len(nome) - nome.count(' ')
        
print("Quantidade total de letras: {}".format(quant))

print("Quantidade de letras do primeiro nome: {}".format(len(nomes[0])))

