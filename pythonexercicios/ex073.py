# TUPLAS, BRASILEIRÃO

brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print('Os 5 primeiros colocados:')
for c in brasileirao[:5]:
    print(c)

print('\nOs 4 últimos colocados:')
for c in brasileirao[16:]:
    print(c)

print(f'Em ordem alfabética:\n {sorted(brasileirao)}')

if 'Chapecoense' in brasileirao:
    for c in range(0, len(brasileirao)):
        if brasileirao[c] == 'Chapecoense':
            break
    print(f'O time da Chapecoense está na {c+1}° posição.')
else:
    print(f'O time da Chapecoense não está na colocação.')


"""
OU

brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print(f'Os 5 primeiros colocados: {brasileirao[0:5]}')

print(f'\nOs 4 últimos colocados: {brasileirao[16:]}')

print(f'Em ordem alfabética:\n {sorted(brasileirao)}')

if 'Chapecoense' in brasileirao:
    for c in range(0, len(brasileirao)):
        if brasileirao[c] == 'Chapecoense':
            break
    print(f'O time da Chapecoense está na {c+1}° posição.')
else:
    print(f'O time da Chapecoense não está na colocação.')

"""