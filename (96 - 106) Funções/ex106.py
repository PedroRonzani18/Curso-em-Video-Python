"""
Manual help interativo
"""

def ajuda(com):
    help(com)

def titulo(msg):
    t = len(msg) + 4
    print(t*'~')
    print(f"  {msg}  ")
    print(t*'~')


com = ''
while True:
    titulo("Sistema de ajuda")
    com = str(input("Função ou biblioteca: "))
    if(com.upper() == "FIM"): break
    else: ajuda(com)    
