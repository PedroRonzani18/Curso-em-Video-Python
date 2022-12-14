"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
"""

nome = input("Digite seu nome completo: ")
result = nome.upper()

if result.find("SILVA") != -1:
    print("Contém.")
else:
    print("Não contém.")
    
print('SILVA' in nome.upper())