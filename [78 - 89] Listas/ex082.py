"""
Lê varios numeros e adiciona na lista.
Armazena em listas externas valores pares e impares
"""

l = []
i = []
p = []

while(1):
    l.append(int(input("Valor: ")))
    if(input("Continuar: [S/N] ").upper() == "N"): break
    
for j in l:
    if j%2 == 0: p.append(j)
    else: i.append(j)
    
print(f"Original: {l}\nPares: {p}\nÍmpares: {i}")