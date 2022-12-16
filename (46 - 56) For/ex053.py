"""
Confere se frase é palíndromo
"""

f = input("Frase: ").strip()
palavras = f.split()

junto = ''.join(palavras)

for i in range(0,int(len(junto)/2)):
    if junto[i] != junto[len(junto)-i-1]:
        print("Não palíndromo")
        exit()
        
print("Palindromo")
