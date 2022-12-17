"""
Lê produto e preço, armazena em tupla, mostra de maneira tabular
"""

tu = ('aaaaa',1,'b',2,'c',3,'d',4)

for i in range (0,len(tu)):
    if(i % 2 == 0):
        print(f"{tu[i]:.<15}",end='')
    else:
        print(f"{tu[i]:>}")