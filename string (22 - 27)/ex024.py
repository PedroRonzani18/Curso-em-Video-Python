"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
"""

cidade = input("Nome da cidade: ").strip()

comp = cidade[:5].upper()
print(comp == "SANTO")
