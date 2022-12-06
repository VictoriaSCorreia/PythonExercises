# PAR OU ÍMPAR | COMANDO BREAK
from random import randint
cont = 0
while True:
    jogador = int(input('Sua jogada: '))
    escolha = ' '
    while escolha not in 'pi':
        escolha = input('PAR OU ÍMPAR [P/I]? ').lower().strip()[0]
    computer = randint(0, 11)
    total = jogador + computer
    if total % 2 == 0:
        print(f'Você jogou {jogador} e o computador jogou {computer}\n{total} é PAR')
        if escolha == 'i':
            break
        cont += 1
    if total % 2 != 0:
        print(f'Você jogou {jogador} e o computador jogou {computer}\n{total} é ÍMPAR')
        if escolha == 'p':
            break
        cont += 1
print(f'GAME OVER! Você venceu {cont} vezes.')

