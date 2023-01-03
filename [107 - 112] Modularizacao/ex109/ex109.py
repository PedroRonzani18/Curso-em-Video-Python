"""
108 porem com valores formatados e mais viziveis
"""
import ex112.utilidades.moeda as moeda

p = float(input("Valor: "))
print(f"Metade: {moeda.metade(p,True)}")
print(f"Dobro: {moeda.dobro(p,True)}")
print(f"Aumento: {moeda.aumentar(p,10,True)}")
print(f"Diminuir: {moeda.diminuir(p,13,True)}")