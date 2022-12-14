"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente
"""

nome = input("Nome completo: ")
nomes = nome.split()
print("Primeiro nome: {}\nUltimo nome: {}".format(nomes[0],nomes[len(nomes)-1]))