"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seus status de acordo com a tabela abaixo
"""
from math import pow

p = float(input("Peso: "))
a = float(input("Altura: "))

imc = p/pow(a,2)

if imc < 18.5: print("Abaixo do peso")
elif imc < 25: print("Peso ideal")
elif imc < 30: print("Sobrepeso")
elif imc < 40: print("Obesidade")
else: print ("Obesidade mórvbida")