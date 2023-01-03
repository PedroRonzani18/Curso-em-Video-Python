"""
crie uma tupla com 5 numeros aleatórios, depois mostrar numeros e menor e maior
"""

from random import randint

tu = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

#print(f"Tupla: {tu}\nMaior: {sorted(tu)[-1]}\nMenor: {sorted(tu)[0]}")
print(f"Tupla: {tu}\nMaior: {max(tu)}\nMenor: {min(tu)}")