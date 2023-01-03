"""
tupla com palavras, exibir as vogais
"""

tu = ('asdjhvb', 'sdijfg', 'asuhdg', 'oauihsvbd', 'sihedjgv')

vog = 'aeiou'

for i in tu:
    print(f"Vogais em {i}: ",end='')
    for j in range (0,len(i)):
        if(i[j] in vog): print(f"{i[j]} ",end='')
    print()