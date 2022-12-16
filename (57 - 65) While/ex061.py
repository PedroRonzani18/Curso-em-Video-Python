"""
Lê primeiro terpo de uma PA e motra os 10 primeiros termos, usando while
"""

a0 = int(input("Termo incial: "))
r = int(input("Razão: "))

i = 0

while(i<10):
    print(a0 + i*r,end=" ")
    i += 1