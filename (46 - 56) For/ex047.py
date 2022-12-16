"""
Crie um programa que mostre na tela todos os numeros pares
que estão entre 1 e 50
"""
inicial = int(input("Digite intervalo inicial: "))
final = int(input("Digite intervalo final: "))

for i in range(inicial,final+1):
    if i%2 == 0: print(i,end=" ")