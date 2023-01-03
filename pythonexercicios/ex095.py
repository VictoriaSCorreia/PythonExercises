# DICIONÁRIOS, CADASTRO DE JOGADORES 2.0

total = 0
grupo = list()
while True:
    jogador = dict()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Gols'] = list()
    for c in range(0, partidas):
        jogador['Gols'].append(int(input(f'Quantos gols na partida {c+1}? ')))
        total = total + jogador['Gols'][c]
    jogador['Total'] = total
    grupo.append(jogador.copy())
    total = 0
    while True:
        resp = str(input('Quer continuar [S/N]? '))
        if resp in 'SsNn':
            break
    if resp in 'Nn':
        break
print('=' * 71)
print('N°  ', end='')
for i in jogador.keys():
    print(f'{i:<25}', end='')
print()
print('=' * 71)
for k, v in enumerate(grupo):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<25}', end='')
    print()
print('-' * 71)
while True:
    resp = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if resp == 999:
        break
    if resp <= len(grupo) - 1:
        print(f'LEVANTAMENTO DO JOGADOR {grupo[resp]["Nome"].upper()}:')
        for c, g in enumerate(grupo[resp]['Gols']):
            print(f'   => No {c+1}° jogo fez {g} gols.')
    else:
        print(f'Erro! Não existe jogador com o número {resp}.')
