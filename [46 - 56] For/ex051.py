"""
Lê primeiro terpo de uma PA e motra os 10 primeiros termos
"""

a0 = int(input("Termo incial: "))
r = int(input("Razão: "))

for i in range (10):
    print(a0 + i*r,end=" ")