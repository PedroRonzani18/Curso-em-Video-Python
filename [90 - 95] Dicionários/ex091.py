"""
4 jogadores jogam um dado e tem resultados aleatórios.
Guardar esses resultados em um dicionário
Ordenar dicionário, depois mostrar o vencedor
"""

from random import randint
from operator import itemgetter

l = []

for i in range (4):
    aux = {}
    aux['Nome'] = str(input("Nome: "))
    aux['Valor'] = randint(1,6)
    print(f"Valor girado: {aux['Valor']}")
    l.append(aux.copy())
    
l = sorted(l,key=itemgetter('Valor'))

max = -1
p = ''

for i in l:
    if(i['Valor'] > max):
        max = i['Valor']
        p = i['Nome']
        
print(f"Vencedor: {p} com seu {max}")