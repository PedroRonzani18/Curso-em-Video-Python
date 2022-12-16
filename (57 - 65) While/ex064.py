"""
Lê numeros até digitar 999. Depois exibe qunatos nmeros foram digitados e a soma total
"""

cond = 1
quant = 0
soma = 0

while cond:
    quant+=1
    e = int(input("Numero: "))
    if(e == 999):
        break
    soma += e