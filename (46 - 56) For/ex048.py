"""
Crie um programa que soe todos os impartes entre 1 e 500
que são multiplos de 3
"""
inicial = int(input("Digite intervalo inicial: "))
final = int(input("Digite intervalo final: "))

soma = 0
for i in range(inicial,final+1):
    if i%3 == 0: soma+=i
    
print(soma)