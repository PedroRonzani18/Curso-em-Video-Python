"""
Usuário digita expressão.
Programa confere se expressão é valida de acordo com seus parenteses
"""

e = input("Expressão: ")

par = 0
iPar = 0

for i in e:
    if i == "(": par += 1
    elif i == ")": iPar += 1
    
if par == iPar: print("Expressão válida")
else: print("Expressão inválida")