"""
lê 4 valores, armazena em tupla
1. mostra quantas vezes apareceu 9
2. mostra posiçãodo primeiro 3
3. quais foram os pares
"""

aux = []

for i in range (4): aux.append(int(input("Numero: ")))

tu = (aux[0],aux[1],aux[2],aux[3])

print(f"Quantidade de vezes que 9 apreceu: {tu.count(9)}")

try: print(f"Posição do peimeiro 3: {tu.index(3)}")
except: print("Você não digitou o numero 3")

print(f"Numeros pares: ",end='')

for i in tu:
    if(i%2 == 0): print(f"{i}, ",end='')