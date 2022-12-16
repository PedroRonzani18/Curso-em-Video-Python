"""
Faça um programa que mostre na tela uma contagem refressiva
de 10 até zero com uma pausa de 1 segundo entre elas
"""

from time import sleep

for i in range(10,-1,-1):
    print(i)
    sleep(1)

