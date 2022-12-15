"""
Faça um programa  que leia o ano de nascimentoi de um jovem e informe:
- se ele ainda vai se alistar ao serviço militar
- se é a hora de se alistar
- se já passou do tempo de alistamento
O programa deve mostrar o tempo que falta ou que passou do prazo
"""

import datetime

atual = datetime.date.today().year
ano = int(input("Digite seu ano de nascimento: "))
d = atual - ano

if d < 18: print("Vai se alistar em {} anos".format(18-d))
elif d == 18: print("Hora de se alistar")
elif d > 18: print("Era pra ter se alistado {} anos atrás hein".format(d-18))