"""
Lê primeiro terpo de uma PA e motra os 10 primeiros termos, usando while, e perguntando se o usuario quer ver mais numeros
"""

a0 = int(input("Termo incial: "))
r = int(input("Razão: "))

i = 0
an = 0

while(i<10):
    an = a0 + i*r
    print(an,end=" ")
    i += 1
    
mais = 1
while(mais != 0):
   mais = int(input("\nQuer ver mais quantos numeros: "))
   
   for j in range (1,mais+1):
       an = an +  r
       print(an,end=" ")

   