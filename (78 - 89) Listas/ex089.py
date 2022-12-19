"""
Lê nome e 2 notas de vários alunos.
Exibir um boletim com a média de cada aluno.
Permitir que usuiario possa ver notas individuais de cada aluno.
"""

alunos = []

while(True):
    aux = []
    aux.append(str(input("Nome: ")))
    aux.append(int(input("Nota 1: ")))
    aux.append(int(input("Nota 2: ")))
    alunos.append(aux[:])
    
    if(str(input("Adicionar? [S/N] ")).upper() == "N"): break
    
for i in range (len(alunos)):
    print(f"{alunos[i][0]} : {(alunos[i][1] + alunos[i][2])/2}")  
    
while(True):
    if(str(input("Deseja ver as notas individuais de algum aluno? [S/N] ")).upper() == "N"): break
    
    aux = input("Aluno: ")
    
    found = False
    
    for aluno in alunos:
        if aluno[0] == aux:
            found = True
            print(f"Notas: {aluno[1]} , {aluno[2]}")
            break
        
    if(found == False): print("Aluno não cadastrado")
