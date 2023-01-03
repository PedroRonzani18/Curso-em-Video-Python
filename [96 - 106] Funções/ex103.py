"""
Programa que recebe parametros opcionais
"""

def ficha(jogador = "<desconhecido", gols = "0"):
    print(f"O jogador {jogador} fez {gols} gols no campeonato")
    

jogador = str(input("Nome do jogador: "))
gols = str(input("Numero de gols: "))

if(jogador.strip() == "") and (gols == ""): ficha()
elif(jogador.strip() == ""): ficha(gols=gols)
elif(gols == ""): ficha(jogador)
else: ficha(jogador,gols)
