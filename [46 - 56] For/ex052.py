"""
Verifica se é primo
"""

n = int(input("Numero: "))

for i in range (2,n):
    if n % i == 0: 
        print("Não primo")
        exit()
    
print("Primo")
