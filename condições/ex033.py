"""
Programa que lê 3 numeros e indica o maior e o menor
"""

valores = []

for i in range (3):
    valores.append(int(input("Numero {}: ".format(i+1))))

valores.sort()

print("Menor: {}\nMaior: {}".format(valores[0],valores[len(valores)-1]))