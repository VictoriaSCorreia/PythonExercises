# CADASTRO DE PESSOAS | COMANDO BREAK
idadeC = homensC = mulheresC = 0
while True:
    print(f'{"=" * 21}\n CADASTRO UMA PESSOA \n{"=" * 21}')
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
        if sexo in 'mf':
            break
    if idade >= 18:
        idadeC += 1
    if sexo == 'm':
        homensC += 1
    if sexo == 'f' and idade < 20:
        mulheresC += 1
    while True:
        escolha = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
        if escolha in 'sn':
            break
    if escolha == 'n':
        break
print(f'{idadeC} pessoas possuem mais de 18 anos.\n{homensC} homens foram cadastrados.\n{mulheresC} mulheres '
      f'com menos de 20 anos foram cadastradas.')


"""
idadeC = homensC = mulheresC = 0
while True:
    print(f'{"=" * 21}\n CADASTRO UMA PESSOA \n{"=" * 21}')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    if idade >= 18:
        idadeC += 1
    if sexo == 'm':
        homensC += 1
    if sexo == 'f' and idade < 20:
        mulheresC += 1
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
    if escolha == 'n':
        break
print(f'{idadeC} pessoas possuem mais de 18 anos.\n{homensC} homens foram cadastrados.\n{mulheresC} mulheres '
      f'com menos de 20 anos foram cadastradas.')
"""