def moeda(p):
    return f"{p:.2f}".replace('.',',')

def aumentar(p,a,formated):
    if(formated == False): return p * (1+a/100)
    else:                  return moeda(p* (1+a/100))

def diminuir(p,r,formated):
    if(formated == False): return p * (1-r/100)
    else:                  return moeda(p * (1-r/100))

def metade(p,formated):
    if(formated == False): return p/2
    else:                  return moeda(p/2)

def dobro(p,formated):
    if(formated == False): return p*2
    else:                  return moeda(p*2)   