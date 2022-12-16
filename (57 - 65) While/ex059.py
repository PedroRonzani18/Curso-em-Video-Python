"""
Programa de calculadora simples
"""

import math

while 1:
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))

    match int(input("\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\n\nEscolha sua operação: ")):
        case 1:
            print("{} + {} = {}".format(a,b,a+b))
            exit()
        case 2:
            print("{} * {} = {}".format(a,b,a*b))
            exit()
        case 3:
            print("Maior numero: {}".format(max(a,b)))
            exit()
        case 5:
            exit()
    