"""
Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
O programa deverá escrever na tela se o usuário vençeu ou perdeu.
"""

import random

r = random.randint(0,5)
t = int(input("Tentativa: "))

if t == r: print("Certo")
else: print("Errado, era {}".format(r))
    