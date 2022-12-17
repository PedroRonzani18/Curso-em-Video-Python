"""
Lê nome e preço, para quando usuario quiser
1. total gasto
2. quantos > 1000
3. produto mais barato
"""

total = 0
caros = 0
baratoP = float("inf")
baratoN = ""

while(1):
    n = input("Nome: ")
    p = float(input("Preço: "))
    
    total += p
    if(p > 1000): caros += 1
    if(p < baratoP):
        baratoP = p
        baratoN = n
        
    if(input("Deseja continuar [S/N] : ").upper() == "N"): break   
    
print(f"Total: {total}\nCaros: {caros}\nProduto mais barato: {baratoN}")
    