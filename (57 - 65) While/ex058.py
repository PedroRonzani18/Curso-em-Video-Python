"""
Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 10
e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
O jogador tenta advinhar até acertar 
"""

import random

cond = 1
i=0
r = random.randint(0,10)

while cond:
    i+=1
    t = int(input("Tentativa: "))
    if t == r: cond = 0
    
print("Você venceu com {} tentativas".format(i))