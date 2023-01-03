import random

nomes = []

for i in range (4):
    nomes.append(input("Nome {}: ".format(i+1)))
    
r = random.randint(1,4)

print("Escolhido: {}".format(nomes[r-1]))
print("Escolhido: {}".format(random.choice(nomes)))