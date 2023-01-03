"""
Programa que lê 6 inteiros e soma apenas pares
"""

soma  = 0

for i in range(6):
    temp = int(input("Numero: "))
    if temp % 2 == 0: soma += temp
    
print (soma)