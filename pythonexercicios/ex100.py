# FUNÇÕES, SORTEAR E SOMAR

from random import randint
def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 5))
    print(f'Sorteando os 5 valores da lista... {lista}')
def somaPar(valores):
    soma = 0
    for n in valores:
        if n % 2 == 0:
            soma += n
    print(f'A soma de todos os valores pares da lista é {soma}')


valores = list()
sorteia(valores)
somaPar(valores)

''' 
OU

from random import randint
def sorteia():
    numeros = list()
    for c in range(0, 5):
        numeros.append(randint(1, 5))
    print(f'Sorteando os 5 valores da lista... {numeros}')
    return numeros
def somaPar(valores):
    soma = 0
    for n in valores:
        if n % 2 == 0:
            soma += n
    print(f'A soma de todos os valores pares da lista é {soma}')


valores = list(sorteia())
somaPar(valores)

'''
