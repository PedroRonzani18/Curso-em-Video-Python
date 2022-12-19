"""
Usuário digita 7 valores e cadastra ele em uma lista
com duas listas: uma pra par, outra pra impar 
"""

li = [[],[]]

for i in range (7):
    e = int(input("Numero: "))
    if(e%2 == 0): li[0].append(e)
    else:         li[1].append(e)

li[0].sort()
li[1].sort()

print(f"Pares: {li[0]}\nÍmpares: {li[1]}")