"""
Escreva um programa que leia a velocudade de um carro.
Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo
que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
"""

velocidade = int(input("Velocidade: "))

if velocidade >= 80:
    print("Multa: R$ {},00".format((velocidade-80)*7))