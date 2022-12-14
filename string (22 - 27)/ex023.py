"""
Faça um programa que leira um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
"""

num = int(input("Digite um numero de 0 a 9999:"))

print("Unidade: {}".format(num%10))
if num > 9:
    #print("Dezena: {}".format(int((num%100)/10)))
    print("Dezena: {}".format(int(num // 10 % 10)))
if num > 99:
    #print("Centena: {}".format(int((num%1000)/100)))
    print("Centena: {}".format(int(num // 100 % 10)))
if num > 999:
    #print("Unidade de milhar: {}".format(int((num%10000)/1000)))
    print("Unidade de milhar: {}".format(int(num // 1000 % 10)))
