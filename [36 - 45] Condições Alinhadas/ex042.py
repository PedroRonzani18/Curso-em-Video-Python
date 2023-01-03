"""
Programa que recebe 3 retas e diz qual tipo de triangulo pode gerar
"""

l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))

if l1+l2>l3 and l1+l2>l2 and l2+l3>l1:
    if l1 == l2 == l3: print("Equilatero")
    elif l1 != l2 != l3 != l1: print("Escaleno")
    else: print("Isósceles")
else: print("Não é possivel gerar um triângulo")