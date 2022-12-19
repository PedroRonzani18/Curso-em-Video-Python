"""
Criar uma matriz 3x3
"""

mat = []

for i in range (3):
    aux = []
    for j in range (3):
        aux.append(int(input(f"[{i}][{j}]: ")))
    mat.append(aux[:])
    
print()

for i in range(3):
    for j in range (3):
        print(f"[{mat[i][j]}] ",end='')
    print()
print()