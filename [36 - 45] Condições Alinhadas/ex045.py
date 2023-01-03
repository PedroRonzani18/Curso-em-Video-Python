"""
Programa que joga Jokenpô
"""

import random

j = int(input("Pedra = 1 | Papel = 2 | Tesoura = 3\nDigite sua jogada: "))

r = random.randint(1,3)

if   (j==1 and r==1) or (j==2 and r==2) or (j==3 and r==3): print("Empate")
elif (j==1 and r==3) or (j==2 and r==1) or (j==3 and r==2): print("Vitória do jogador")
else: print("Vitória do computador")