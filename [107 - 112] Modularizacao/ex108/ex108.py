"""
107 porem com valores formatados
"""
import ex112.utilidades.moeda as moeda

p = float(input("Valor: "))
print(f"Metade: {moeda.moeda(moeda.metade(p))}\nDobro: {moeda.moeda(moeda.dobro(p))}\nAumento: {moeda.moeda(moeda.aumentar(p,10))}\nDiminuir: {moeda.moeda(moeda.diminuir(p,13))}")