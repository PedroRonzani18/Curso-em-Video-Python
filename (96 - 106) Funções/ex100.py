"""
Sortear 5 numeros e somar seus valores pares usando apenas funções
"""

from random import randint

def sorteia():
    aux = []
    print("Valores gerados: ",end='')
    for i in range (5):
        aux.append(randint(0,10))
        print(f"{aux[i]} ",end='')
    print()
    return aux[:]


def somaPar(valores):
    soma = 0
    
    for i in valores:
        if (i%2 == 0): soma += i
        
    return soma

# main
print(f"Valores pares somados: {somaPar(sorteia())}")