"""
Programa com uma função Área() que recebe diomensões de um terreno e retorne sua área
"""

def area(a,b):
    return a*b


print(f"Area: {area(int(input('Largura: ')), int(input('Altura: ')))}")