"""
Lê nome, ano de nascimento e carteira de trabalho.
Arazena eles e a idade em um dicionario.
Se CTPS for diferente de zero, deve receber ano de contratação e salário.
Calcular com quantos anos a pessoa vai se aposentar (35 anos de trabalho)
"""

import datetime

dic = {}

dic['Nome'] = str(input("Nome: "))

atual = datetime.date.today().year
ano = int(input("Ano de nascimento: "))
d = atual - ano

dic['Idade'] = d
dic['CTPS'] = int(input("Carteira de Trabalho: "))

if(dic['CTPS'] != 0):
    dic['Aposentadoria: '] = int(input('Ano de Contratação: ')) + 35 - ano
    dic['Salário'] = int(input('Salário: '))
    
for k,v in dic.items():
    print(f"{k}: {v}")