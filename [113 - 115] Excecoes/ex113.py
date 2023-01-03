"""
Função leiaint e leiafloat
"""

def leiaInt():
    while(True):
        try:
            i = int(input("Digite um inteiro: "))
        except (ValueError,TypeError):
            print("ERRO: digite um inteiro valido\n")
        except KeyboardInterrupt:
            print("O usuario preferiu nao digitar esse numero.")
            return 0
        else:
            return i
    
def leiaFloat():
    while(True):
        try:
            i = float(input("Digite um Real: "))
        except (ValueError,TypeError):
            print("ERRO: digite um Real valido\n")
        except KeyboardInterrupt:
            print("O usuario preferiu nao digitar esse numero.")
            return 0
        else:
            return i
    
# Main
print(f"O numero inteiro foi {leiaInt()} e o real foi {leiaFloat()}")