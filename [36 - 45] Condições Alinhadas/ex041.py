"""
Programa que leia o ano de nascimento de uma atleta 
e mostre sua categotia de acordo com a idade:
- até 9: mirim
- até 14: infantil
- até 19: junior
- até 20: senior
- acima: master
"""

idade = int(input("Digite sua idade: "))

if idade <=9: print("Mirim")
elif idade <=14: print("Infantil")
elif idade <=19: print("Junior")
elif idade <=20: print("Sênior")
else: print("Master")
