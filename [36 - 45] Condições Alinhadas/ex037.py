"""
Escreva um programa que leia um numero inteiro qualquer e peça para
o usuário escolher qual será a conversão de base
"""
num = int(input("Digite um numero: "))

match int(input("Tipo de conversão: ")):
    case 1: print("Binário: {}".format(bin(num)))
    case 2: print("Octal: {}".format(oct(num)))
    case 3: print("Hexadecimal: {}".format(hex(num)))