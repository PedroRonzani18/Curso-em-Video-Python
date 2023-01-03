"""
Escreva um programa que leia dois numeros inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

a = int(input("Numero 1: "))
b = int(input("Numero 2: "))

if a > b: print("O primeiro valor é maior")
elif a == b: print("Não existe valor maior, os dois são iguais")
elif a < b: print("O segundo valor é maior")