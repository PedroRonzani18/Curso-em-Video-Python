import random

nomes = []

for i in range (4):
    nomes.append(input("Nome {}: ".format(i+1)))
    
random.shuffle(nomes)
print(nomes)
    
'''   
while(len(nomes) > 0):
    r = random.randint(0,len(nomes)-1)
    print ("Escolhido: {}".format(nomes[r]))
    nomes.remove(nomes[r])
'''