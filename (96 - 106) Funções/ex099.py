"""
criar função max() na marra
"""

def maior(*valores):
    maior = valores[0]
    for i in valores:
        if(i > maior): maior = i
    return maior


print(f"Maior valor: {maior(1,3,4,56,67,5,3,2,54,56,4,3,5,7,5,6)}")