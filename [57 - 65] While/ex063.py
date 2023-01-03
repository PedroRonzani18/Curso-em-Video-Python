"""
N primeiros termos de fibonacci
"""

import math

n = int(input("Quantidade de numeros: "))

numeros = []
numeros.append(1)
numeros.append(1)

for i in range (2,n):
    numeros.append(numeros[i-2] + numeros[i-1])
    
for i in range (len(numeros)):
    print(numeros[i],end=' ')