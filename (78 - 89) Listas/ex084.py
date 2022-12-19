"""
Lê nome e peso de várias pessoas, e armazena em lista.
Deposi mostra:
1. total de pessoas cadastradas
2. Listagem das pessoas mais pesadas
3. Listagem das pessoas mais leves
"""
l = []

while(1):
    aux = []
    n = str(input("Nome: "))
    p = float(input("Peso: "))
    
    aux.append(n)
    aux.append(p)
    
    l.append(aux[:])
    
    if(str(input("Continuar? [S/N] ")).upper() == "N"): break

max = -1
min = float("inf")

for i in l:
    if i[1] > max: max = i[1]
    if i[1] < min: min = i[1]

print(f"{len(l)} pessoas cadastradas\nPessoas pesadas: ",end='')

for i in l:
    if i[1] == max: print(f"{i[0]} ",end='')
print()

print(f"Pessoas leves: ",end='')

for i in l:
    if i[1] == min: print(f"{i[0]} ",end='')
print()
    

    