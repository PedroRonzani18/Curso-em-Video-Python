"""
Usuário digita 5 valores que devem entrar em uma lista ordenada sem sort()
"""

l = []
l.append(int(input("Valor: ")))

for i in range (4):
    e = int(input("Valor: "))
    cond = 1
    for j in range(len(l)):
        if(l[j] >= e and cond) :
            l.insert(j,e)
            cond = 0
    if(cond): l.append(e)

print(l)
    