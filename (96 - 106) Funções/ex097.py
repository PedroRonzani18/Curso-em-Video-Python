"""
Função escreva, que recebe texto e imprime na tela com tamanho adaptável
"""

def escreva(txt):
    i = len(txt)
    print('~' * (i+2))
    print(f' {txt} ')
    print('~' * (i+2))
    
    
escreva(str(input("Texto a ser exibido: ")))