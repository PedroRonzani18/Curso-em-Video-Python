"""
Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final, 
de acordo com a média atingida
- reprovado < 5
- recuperação 5 <= x <= 6.9
- aprovado >=7
"""

num = int(input("Quantidade de notas a cadastrar: "))
soma = 0

for i in range (num):
    soma += float(input("Nota {}: ".format(i+1)))
    
media = soma/num

if media <= 5: print("Reprovado")
elif 5 < media and media < 7: print("Recuperação")
elif media >= 7: print("Aprovado")