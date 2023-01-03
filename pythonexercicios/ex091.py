# DICIONÁRIOS, JOGO DE DADOS

from random import randint
jogadores = dict()
rank = list()
cont = 0
for j in range(0, 4):
    jogadores[f'jogador{j+1}'] = randint(1, 6)
    print(f'O jogador{j+1} tirou {jogadores[f"jogador{j+1}"]}')
for v in jogadores.values():
    if rank.count(v) < 1:
        rank.append(v)
rank.sort(reverse= True) 
for n in rank:
    for j, v in jogadores.items():
        if v == n:
            cont += 1
            print(f'{cont}° LUGAR: {j} com {v}')
  
'''
OU

from random import randint
from operator import itemgetter
jogadores = {'jogador1':  randint(1, 6), 'jogador2':  randint(1, 6),
'jogador3':  randint(1, 6), 'jogador4':  randint(1, 6)}
rank = list()
cont = 0
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
rank = sorted(jogadores.items(), key=itemgetter(1), reverse= True) 
for p, v in enumerate(rank):
    print(f'{p+1}° lugar: {v[0]} com {v[1]}.') 

'''
