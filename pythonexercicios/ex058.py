# Jogo da advinhação 2.0
from random import randint
num = randint(0, 10)
escolha = 11
cont = 0
print('DUVIDO VOCÊ ADVINHAR EM QUE NÚMERO DE 0 À 10 ESTOU PENSANDO!')
while escolha != num:
    cont += 1
    if cont == 1:
        escolha = int(input('Faça sua jogada: '))
    else:
        if escolha < num:
            escolha = int(input('Mais... Tente novamente: '))
        if escolha > num:
            escolha = int(input('Menos... Tente novamente: '))
print('{}!'.format(num))
if cont > 1:
    print('Você precisou de {} tentativas para me vencer!'.format(cont))
else:
    print('Você precisou de {} tentativa para me vencer!'.format(cont))

"""
OU

from random import randint
num = randint(0, 10)
acertou = False
escolha = 11
cont = 0
print('DUVIDO VOCÊ ADVINHAR EM QUE NÚMERO DE 0 À 10 ESTOU PENSANDO!')
while not acertou:
    cont += 1
    if cont == 1:
        escolha = int(input('Faça sua jogada: '))
    else:
        if escolha < num:
            escolha = int(input('Mais... Tente novamente: '))
        if escolha > num:
            escolha = int(input('Menos... Tente novamente: '))
    if escolha == num:
        acertou = True
print('{}!'.format(num))
if cont > 1:
    print('Você precisou de {} tentativas para me vencer!'.format(cont))
else:
    print('Você precisou de {} tentativa para me vencer!'.format(cont))
    
"""