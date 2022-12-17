"""
Tabuada de vários numeros. para com numero negativo
"""

while(1):
    e = int(input("Numero: "))
    if(e<0): break
    
    for i in range (11):
        print(f"{e} x {i} = {e*i}")
