"""
Lê varios valores e adiciona na lista até usuario não querer mais.
Exibir ao final:
1. quantos numeros foram digitados
2. lista de valores decrescentes
3. se 5 está na lista
"""

l = []
quant = 0

while(True):
    l.append(int(input("Valor: ")))
    if(input("Continuar? [S/N] ").upper() == 'N'): break
    
print(f"Quantidade de numeros adiiconados: {quant}\nLista decrescente: {l.sort(reverse=True)}\n5 Está na lista: {l.__contains__(5)}")