# PEDRA, PAPEL E TESOURA

from random import choice
from time import sleep

resp = input('Pedra, papel ou tesoura? ').lower().strip()

ppt = ['pedra', 'papel', 'tesoura']
escolha = choice(ppt)

if resp == 'pedra' or resp == 'papel' or resp == 'tesoura':

    sleep(0.3)
    print('\nJO'), sleep(0.4)
    print('KENN...'), sleep(0.4)
    print('PÔ!'), sleep(0.3)

    print('{:^20}'.format(escolha + '!').upper())
    if escolha == resp:
        print(' Pare de me copiar!')
    elif resp == 'pedra' and escolha == 'papel':
        print('     Eu ganhei.')
    elif resp == 'pedra' and escolha == 'tesoura':
        print('   Você ganhou...')
    elif resp == 'tesoura' and escolha == 'pedra':
        print('     Eu ganhei.')
    elif resp == 'tesoura' and escolha == 'papel':
        print('   Você ganhou...')
    elif resp == 'papel' and escolha == 'tesoura':
        print('     Eu ganhei.')
    elif resp == 'papel' and escolha == 'pedra':
        print('   Você ganhou...')

else:
    print('   Digite direito!')
