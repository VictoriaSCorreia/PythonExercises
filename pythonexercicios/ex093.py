# DICIONÁRIOS, CADASTRO DE JOGADORES

jogador = {'Nome': str(input('Nome do Jogador: '))}
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
jogador['Gols'] = list()
total = 0
for c in range(0, partidas):
    jogador['Gols'].append(int(input(f'Quantos gols na partida {c+1}? ')))
    total = total + jogador['Gols'][c]
jogador['Total'] = total
print('=' * 71)
print(jogador)
print('=' * 71)
for j, v in jogador.items():
    print(f'No campo "{j}" tem: {v}.')
print('=' * 71)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for p, g in enumerate(jogador['Gols']):
    print(f'     => Na {p+1}° partida fez {g} gols. ')
print(f'Foi um TOTAL de {jogador["Total"]} gols.')
