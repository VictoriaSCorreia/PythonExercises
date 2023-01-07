# FUNÇÕES, BOLETIM DO ALUNO

def notas(*notas, sit=False):
    boletim = {}
    boletim['Total'] = len(notas)
    boletim['Maior'] = max(notas)
    boletim['Menor'] = min(notas)
    boletim['Média'] = sum(notas)/len(notas)
    if sit:
        if boletim['Média'] >= 7:
            boletim['Situação'] = 'Acima da média'
        else:
            boletim['Situação'] = 'Abaixo da média'
    return boletim
alunos = notas(5.6, 7.0, 8.9, 8.9, 7.1, sit=True)
print(alunos)


'''
def notas(*notas, sit=False):
    soma = 0
    boletim = {}
    boletim['Total'] = len(notas)
    boletim['Maior'] = max(notas)
    boletim['Menor'] = min(notas)
    for c in range(0, len(notas), 1):
        soma += notas[c]
    boletim['Média'] = soma/len(notas)
    if sit:
        if boletim['Média'] >= 7:
            boletim['Situação'] = 'Acima da média'
        else:
            boletim['Situação'] = 'Abaixo da média'
    return boletim
alunos = notas(5.6, 7.0, 8.9, 8.9, 7.1, sit=True)
print(alunos)
'''