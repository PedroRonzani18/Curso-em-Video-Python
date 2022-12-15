"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens
de até 200 Km, e R$0,45 para viagens mais longas.
"""

km = int(input("Quilometragem: "))

if km <= 200: print("Valor: R${:.2f}".format(0.5*km))
else: print("Valor: R${:.2f}".format(0.45*km))