"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário 
ou então o empréstimo será negado.
"""

c = float(input("Valor da casa: "))
s = float(input("Valor do salario: "))
a = float(input("Valor de anos: "))
p = c/(a*12)
if p <= s*0.3: print ("Prestação: {}".format(p))
else: print ("Empréstimo negado")
