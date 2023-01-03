def aumentar(p,a):
    return p* (1+a/100)

def diminuir(p,r):
    return p * (1-r/100)

def metade(p):
    return p/2

def dobro(p):
    return p*2

def moeda(p):
    """
    inteiro = p//1
    decimal = p%1
    
    decimais = []
    decimais.append((decimal*10)//1)
    decimal = (decimal * 10) - ((decimal*10)//1)
    decimais.append((decimal*10)//1)
    
    return str(int(inteiro)) + "," + str(int(decimais[0])) + str(int(decimais[1]))
    """
    return f"{p:.2f}".replace('.',',')