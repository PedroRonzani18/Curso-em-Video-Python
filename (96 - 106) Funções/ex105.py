"""
Função notas que recebe varias notas e retorna dicionario com:
1. quantidade de notas
2. maior nota
3. menor nota
4. media da tuma
5. a situação da turma
"""

def notas(*nota, sit=False):
    """_summary_
    -> Função para analisar notas e situações de vários alunos
    Args:
        nota: uma ou mais notas dos alunos
        sit: valor opcional, indicando se deve ou mão adicionar a situação

    Returns:
        dicionario com várias informações dobre a situação da turma
    """
    soma = 0
    for i in nota:
        soma += i
    
    retorno = {}
    retorno["Total"] = len(nota)
    retorno["Maior"] = max(nota)
    retorno["Menor"] = min(nota)
    retorno["Media"] = soma/len(nota)
    
    if(sit):
        if(retorno["Media"] < 6): retorno["Situação"] = "RUIM"
        elif(retorno["Media"] >= 6 and retorno["Media"] < 7) : retorno["Situação"] = "RAZOAVEL"
        else:                        retorno["Situação"] = "BOA"
        
    return retorno


help(notas)