"""
Lê o nome de vários jogadore e quantas partidas ele jogou.
Lê quantidade de gols em cada partida.
Tudo será armazenado em um dicionário, incluindo o total de gols.
"""

jogadores = []

while(True):
    jogador = {}

    print("-"*30)
    jogador['Nome'] = str(input("Nome: "))
    jogador['Partidas'] = int(input("Quantidade de partidas jogadas: "))

    gols = []
    soma = 0

    for i in range (jogador['Partidas']):
        gols.append(int(input(f"Gols marcados na partida {i+1}: ")))

    jogador['Gols em cada partida'] = gols

    for i in gols:
        soma += i

    jogador['Soma dos gols'] = soma
    jogadores.append(jogador.copy())
    
    if(str(input("Adicionar mais jogadores? (S/N) ")).upper() == 'N'): break

print("=-"*15)
for j in jogadores:
    for k,v in j.items():
        print(f"{v}",end='   ')
    print()
print("=-"*15)
    
while(True):
    if(str(input("Deseja ler algo específico de um jogador? (S/N) ")).upper() == "N"): break
    n = str(input("Nome do jogador: "))
    
    flag = False
        
    for j in jogadores:
        if(j['Nome'] == n):
            flag = True
            for i,g in enumerate(j['Gols em cada partida']):
                print(f"{g} gols na partida {i+1}")
                
    if(flag == False): print("Nome inválido.")
    print("-"*30)
