"""
Elabore um programa que calcule o valor a ser pago
por um produto, considrando seu preço normal e
condição de pagamento
- a vista dinheiro/cheque: 10% desconto
- a vista no cartão: 5% desconto
- 2x no cartão: normal
- 3x no cartão: 20% juros
"""

p = float(input("Valor: "))
modo = input("Modo de pagamento: ")

if modo.find("vista") != -1:
    if modo.find("dinheiro") != -1: print("Valor novo: {}".format(p*0.9))
    elif modo.find("cartão") != -1: print("Valor novo: {}".format(p*0.95))
elif modo.find("x") != -1:
    if modo.find("2x") != -1: print("Valor novo: {}".format(p))
    elif modo.find("3x") != -1: print("Valor novo: {}".format(p*1.2))