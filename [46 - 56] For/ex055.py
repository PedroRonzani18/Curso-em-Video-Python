"""
Lê 5 numeros, encontra maior e menor
"""

num = []

for i in range (5):
    num.append(int(input("Valor: ")))

num.sort()

print("Maior: {}\nMenor: {}".format(num[len(num)-1],num[0]))