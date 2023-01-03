"""
Lê numeros até digitar 999. Depois exibe qunatos nmeros foram digitados e a soma total
"""

quant = 0
soma = 0

while True:
    quant+=1
    e = int(input("Numero: "))
    if(e == 999):
        break
    else: soma += e
    
print(f"Soma: {soma}\nQuant: {quant}")

