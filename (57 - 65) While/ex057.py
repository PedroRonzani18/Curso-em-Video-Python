"""
Programa que lê apenas 'M' ou 'F'. caso outro valor seja digitado, pedir nova entrada
"""

cond = 1

while cond:
    e = input("Entrada: ")
    e = e.upper()
    if e == "M" or e == "F":
        cond = 0
        
