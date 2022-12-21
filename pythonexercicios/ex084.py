# LISTAS COMPOSTAS, ANÁLISE DE DADOS

grupo = []
pessoa = []
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa[:])
    pessoa.clear() 
    while True:
        resp = input('Quer continuar: [S/N] ').strip().upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print(f'\n{len(grupo)} pessoas foram cadastradas.')
for p in grupo:
    if grupo.index(p) == 0:
        maiorpeso = menorpeso = p[1]
    else:
        if p[1] >= maiorpeso:
            maiorpeso = p[1]
        elif p[1] <= menorpeso:
            menorpeso = p[1]
print(f'O maior peso foi de {maiorpeso}Kg de: ', end=' ')
for p in grupo:
    if p[1] == maiorpeso:
        print(f'{p[0]}...', end=' ')
print(f'\nO menor peso foi de {menorpeso}Kg de: ', end=' ')
for p in grupo:
    if p[1] == menorpeso:
        print(f'{p[0]}...', end=' ')
