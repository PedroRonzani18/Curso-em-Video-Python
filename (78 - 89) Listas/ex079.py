"""
Usuário digita valores a serem cadastrados em uma lista.
Caso o número ja exista, não será adicionado.
No final, serão exibidos apenas valores únicos.
"""

v = []

while(1):
    e = int(input("valor: "))
    
    if(e in v): print("Valor já presente")
    else: 
        v.append(e)
        print("Valor adicionado com sucesso")
        
    if(input("Continuar? [S/N] ").upper() == "N"): break
    
print(f"Valores digitados: {v}")