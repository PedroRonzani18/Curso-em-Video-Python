"""
Criar lista que armazela listas menores
"""

from random import randint
import time

n = int(input("Quantidade de palpites: "))

palpites = []
numeros = []

for i in range(60): numeros.append(i+1)

for i in range(n):
    aux = []
    for j in range(6):
        e = numeros[randint(0,len(numeros)-1)]
        aux.append(e)
        numeros.remove(e)
    palpites.append(aux[:])
    
for i in range(n):
    print(f"Palpite {i+1}: {palpites[i]}")
    time.sleep(1)