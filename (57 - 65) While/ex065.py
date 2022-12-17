"""
Programa que leia vários numeros inteiros.
Mostra média, menor num lido e se quer continuar
"""

import math

menor = float("inf")
i = 0
soma = i

while(True):
    e = int(input("Numero: "))
    if(e < menor): menor = e
    soma += e
    i += 1
    c = int(input("Deseja continuar? 1 ou 0: "))
    if (c == 0): break
    
print(f"Média: {soma/i}\nMenor: {menor}")
    