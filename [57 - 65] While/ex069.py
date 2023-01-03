"""
Programa que lê idade e sexo de pessoas até condição de parada, depois mostra:
1. quantos são >18
2. Quantos homens
3. Quantas mulheres <20
"""

mai18 = 0
homens = 0
mulhNova = 0

while(1):
    s = input("Sexo (M ou F): ")
    s = s.upper()
    i = int(input("Idade: "))
    
    if(i > 18): mai18 += 1
    
    if(s == "M"): homens += 1
    elif(i < 20): mulhNova += 1
    
    if(int(input("Quer continuar(1 ou 0): ")) == 0): break

print(f"Maiores de 18: {mai18}\nHomens: {homens}\nMulheres < 20: {mulhNova}")    
    