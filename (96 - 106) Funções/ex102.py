"""
Função fatorial com vaiavel de mopstrar processo de fatorial
"""

from time import sleep

def fatorial(n, control):
    """Calcula o fatorial de um número.
    Args:
        n (int): numero cujo fatorial será calculado.
        control (str): 'S' mostra o calculo do fatorial

    Returns:
        int: fatorial de n
    """
    
    fat = 1
    
    while n>0:
        if(control == 'S' and n > 0): 
            print(f"{n} ",end='')
            if(n > 1): print(f"x ",end='')
        fat *= n
        n -=1

    
    return fat
    
print(f'= {fatorial(int(input("Numero: ")),str(input("Quer ver o processo? [S/N] ")))}')
help(fatorial)