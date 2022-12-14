"""
Programa que calcule aumentio de salário:
Se for maior que 1250, aumentar 10%, caso contrário, aumentar 15%
"""

n = int(input("Valor: "))

if n > 1250: print("Novo: {}".format(n * 1.1))
else: print("Novo: {}".format(n * 1.15))