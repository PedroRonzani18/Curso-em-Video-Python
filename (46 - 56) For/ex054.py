"""
Lê nascimento de 7 pessoas e confere quantos são de maior
"""

import datetime

current  = datetime.date.today().year

quant = 0

for i in range (7):
    if(current - int(input("Ano de nascimento: ")) >= 18):
        quant+=1
        
print("{} maior, {} menor".format(quant,7-quant))