import math

a = float(input("Numero: "))
print("Parte inteira: {:.0f}\nParte decimal: {:.2}".format(a//1,a-a//1))
print("Parte inteira: {}\nParte decimal: {:.2}".format(math.trunc(a),a-a//1))
print("Parte inteira: {}\nParte decimal: {:.2}".format(int(a),a-a//1))
