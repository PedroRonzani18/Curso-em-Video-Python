"""
Programa que descobre se a psessoa temvoto negado, opcional ou obrigatório
"""

import datetime

def voto(ano):
    i = datetime.date.today().year - ano
    if i<16: return 'NEGADO'
    if i<18: return 'OPCIONAL'
    return 'OBRIGATÓRIO'

print(f"Voto: {voto(int(input('Ano de nascimento: ')))}")