import math

o = float(input("Cateto Oposto: "))
a = float(input("Cateto Adjacente: "))
print("Hipotenusa: {}".format(math.sqrt(pow(o,2) + pow(a,2))))
print("Hipotenusa: {}".format(math.hypot(o,a)))
