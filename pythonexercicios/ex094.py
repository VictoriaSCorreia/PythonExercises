# DICIONÁRIOS COM LISTAS

grupo = list()
soma = 0
while True:
    pessoa = dict()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [F/M]: '))
        if pessoa['Sexo'] in 'FfmM':
            break
    pessoa['Idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    soma += pessoa['Idade']
    resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break
print(grupo)
print(f'{len(grupo)} pessoas foram cadastradas.')
print(f'{soma/len(grupo):.0f} foi a média de idade.')
print('Mulheres cadastradas: ')
for m in grupo:
    if m['Sexo'] in 'Ff':
        print(f'    => {m["Nome"].upper()}')
print(f'Pessoas com a idade acima da média: ')
for p in grupo:
    if p['Idade'] > soma/len(grupo):
        print(f'    => Nome: {p["Nome"].upper()}; Sexo: {p["Sexo"].upper()}; Idade: {p["Idade"]}')
