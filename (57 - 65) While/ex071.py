"""
Informa valor e retorna quantidade de cedulas
"""

v = int(input("Valor: "))

n = v//50
if(n > 0): print(f"{n} notas de 50")
v -= n*50

n = v//20
if(n > 0): print(f"{n} notas de 20")
v -= n*20

n = v//10
if(n > 0): print(f"{n} notas de 10")
v -= n*10

n = v//1
if(n > 0): print(f"{n} notas de 1")
v -= n*1