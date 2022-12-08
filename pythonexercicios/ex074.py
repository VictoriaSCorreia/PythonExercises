# TUPLAS, MENOR E MAIOR VALORES

from random import randint
menor = 11
maior = 0
tupla = (randint(1, 10), randint(1, 10), 
randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {tupla}')
for c in tupla:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')


"""
OU

from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')
"""