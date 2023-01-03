"""
Lê nome e média de aluno e armazena em um dicionário.
Depois armazena a situação do aluno.
Depois mostra o conteúdo.
"""
dic = {}

dic['Nome'] = str(input("Nome: "))
dic['Média'] = int(input("Media: "))

if(dic['Média'] < 6): dic['Situação'] = 'Reprovado'
else:                 dic['Situação'] = 'Aprovado'

print(dic)