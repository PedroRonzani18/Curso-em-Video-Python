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

def moeda(p):
    return f"{p:.2f}".replace('.',',')

def resumo(preco, aumento, reducao):
    valores = {}
    valores["Preco analisado"] = f"{preco:.2f}"
    valores["Metade do preco"] = metade(preco,True)
    valores["Dobro do preco "] = dobro(preco,True)
    valores["Valor aumentado"] = aumentar(preco,aumento,True)
    valores["Valor diminuido"] = diminuir(preco,reducao,True)

    print('-' * 30)
    print("RESUMO DO VALOR".center(30))
    print('-' * 30)    
    for k,v in valores.items():
        print(f"{k}:\t{v:>3}")
    print('-' * 30)    
        
    