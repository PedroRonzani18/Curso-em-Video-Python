"""
Programa que recebe 3 retas e diz se elas podem gerar um triangulo
"""

v = []

for i in range (3):
    v.append(int(input("Valor {}: ".format(i+1))))
    
if v[0] + v[1] > v[2] and v[0] + v[2] > v[1] and v[2] + v[1] > v[0]: print("Pode")
else: print ("Não pode")