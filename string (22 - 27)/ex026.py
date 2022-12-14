"""
Faça um programa que leia uma frase pelo teclado e mostre:
1. Quantas vezes aparece a letra "A"
2. Em que posição ela aparece a primeira vez
3. Em que posição ela aparece a ultima vez
"""

frase = input("Frase: ").lower().strip()

quant = 0
posi = 0
i=0
while i < len(frase):
    if frase[i] == "A" or frase[i] == "a":
        quant+=1
        posi = i
    i+=1
        
if quant==0:
    print("Não contém A")
else:
    print("A apareceu {} vezes, primeiro em {}, e ultimo em {}".format(quant,frase.find('a'),posi))
    print("A apareceu {} vezes, primeiro em {}, e ultimo em {}".format(frase.count('a'),frase.find('a'),frase.rfind('a')))
    