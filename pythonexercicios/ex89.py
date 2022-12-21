# LISTAS COMPOSTAS, BOLETIM

turma = []
while True:
    aluno = input('Nome: ')
    nota1 = float(input('1° nota: '))
    nota2 = float(input('2° nota: '))
    media = (nota1 + nota2)/2
    turma.append([aluno, [nota1, nota2, media]])
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()
        if resp in 'NS':
            break
    if resp == 'N':
        break
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>10}')
print('-'*33)
for c, a in enumerate(turma):
    print(f'{c:<3} {a[0]:<11} {a[1][2]:>7.1f}')
while True:
    resp = (int(input('Mostrar notas de qual aluno? (Digite 999 para parar) ' )))
    if resp == 999:
        break
    if resp <= len(turma) - 1:
        print(f'As notas de {turma[resp][0].upper()} são: {turma[resp][1][0:2]}')

'''

OU

aluno = []
notas = []
turma = []
while True:
    aluno.append(input('Nome: '))
    notas.append(float(input('1° nota: ')))
    notas.append(float(input('2° nota: ')))
    media = (notas[0] + notas[1])/2
    notas.append(media)
    aluno.append(notas[:])
    turma.append(aluno[:])
    notas.clear()
    aluno.clear()
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()
        if resp in 'NS':
            break
    if resp == 'N':
        break
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>10}')
print('-'*33)
for c, a in enumerate(turma):
    print(f'{c:<3} {a[0]:<11} {a[1][2]:>7}')
while True:
    resp = (int(input('Mostrar notas de qual aluno? (Digite 999 para parar) ' )))
    if resp == 999:
        break
    if resp <= len(turma) - 1:
        print(f'As notas de {turma[resp][0].upper()} são: {turma[resp][1][0:2]}')
'''
