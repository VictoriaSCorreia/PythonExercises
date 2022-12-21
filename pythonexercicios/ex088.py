# LISTAS COMPOSTAS, PALPITES MEGA SENA

from random import randint
from time import sleep
jogos = []
jogo = []
resp = int(input('Quantos palpites você irá querer? '))
for c in range(0, resp):
    while True:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
        if len(jogo) == 6:
            jogos.append(jogo[:])
            jogo.clear()
            break
for c, j in enumerate(jogos):
    sleep(0.4)
    print(f'Jogo {c+1}: {sorted(j)}')
    sleep(0.4)