import moeda


def resumo(preco, aumento, reducao):
    valores = {}
    valores["Preco analisado"] = f"{preco:.2f}"
    valores["Metade do preco"] = moeda.metade(preco, True)
    valores["Dobro do preco "] = moeda.dobro(preco, True)
    valores["Valor aumentado"] = moeda.aumentar(preco, aumento, True)
    valores["Valor diminuido"] = moeda.diminuir(preco, reducao, True)

    print('-' * 30)
    print("RESUMO DO VALOR".center(30))
    print('-' * 30)
    for k, v in valores.items():
        print(f"{k}:\t{v:>3}")
    print('-' * 30)
