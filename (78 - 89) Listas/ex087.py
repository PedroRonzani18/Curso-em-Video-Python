"""
Cria matriz, depois mostra:
1. soma de todos os valores digitados
2. soma dos valores da 3 coluna
3. maior valor da 2 linha
"""

mat = []

for i in range(3):
    aux = []
    for j in range(3):
        aux.append(int(input(f"[{i}][{j}]: ")))
    mat.append(aux[:])
    
print()
    
for i in range(3):
    for j in range (3):
        print(f"[{mat[i][j]}] ",end='')
    print()
print()    

somap = 0
somac = 0
        
for i in range (3):
    somac += mat[i][2]
    for j in range(3):
        if(mat[i][j] % 2 == 0 ): somap += mat[i][j]
        
print(f"Soma de todos os pares: {somap}\nSoma da 3 coluna: {somac}\nMaior valor da 2 linha: {max(mat[1])}")
    
