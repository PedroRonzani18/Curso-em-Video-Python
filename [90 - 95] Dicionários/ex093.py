"""
Lê o nome do jogador e quantas partidas ele jogou.
Lê quantidade de gols em cada partida.
Tudo será armazenado em um dicionário, incluindo o total de gols.
"""

jogador = {}

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

for k,v in jogador.items():
    print(f"{k}: {v}")