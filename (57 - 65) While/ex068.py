"""
Par ou impar até jogador perder
"""
import random

i = 0

while(1):
    e = input("Par(P) ou Ímpar(I): ")

    resto = 0

    match e:
        case "P": resto = 0 
        case "I": resto = 1
        
    n = int(input("Numero: "))

    r = random.randint(0,1)

    if((n+r)%2 == resto): print("Vitória, jogue novamente")
    else: break
    
print(f"Você venceu {i} vezes")
    