"""
Programa que lê 5 valores e guarda em uma lista.
Mostre qual o maior e menor valores digitados e suas posições na lista.
"""

l = []

for i in range(5): l.append(int(input("Numero: ")))

print(f"Maior numéro: {max(l)}, posição {l.index(max(l)) + 1}")
print(f"Menor numéro: {min(l)}, posição {l.index(min(l)) + 1}")