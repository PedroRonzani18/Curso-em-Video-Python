"""
Lê nome, sexo, idade de várias pessoas e armazena em vários dicionários
todos dentro de uma lista.
Depois exibe:
1. quantas pessoas foram cadastradas
2. média das idades do grupo
3. lista com todas as mulheres
4. lista com todas as pessoas com idade acima da média
"""

pessoas = []

while(True):
    pessoa = {}
    pessoa['Nome'] = str(input("Nome: "))
    pessoa['Sexo'] = str(input("Sexo (M/F): ").upper())
    pessoa['Idade'] = int(input("Idade: "))
    pessoas.append(pessoa.copy())
    if(str(input("Adicionar mais pessoas? (S/N) ")).upper() == 'N'): break
   
print(f"Quantidade de pessoas cadastradas: {len(pessoas)}")

soma = 0

for p in pessoas: soma += p['Idade']

print(f"Média das idades: {soma/len(pessoas):.2f}")
print("Mulheres cadastradas: ",end='')

for p in pessoas:
    if(p['Sexo'] == 'F'):
        print(f"{p['Nome']} ",end='')
print()
        
print("Pessoas com idade acima da média: ",end='')

for p in pessoas:
    if(p['Idade'] > soma/len(pessoas)): print(f"{p['Nome']} ",end='')
