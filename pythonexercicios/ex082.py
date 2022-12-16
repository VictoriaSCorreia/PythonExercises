# LISTAS, NUMEROS PARES E IMPARES

numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break
for c in numeros:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'Todos os números digitados: {numeros}')
print(f'Números pares digitados: {pares}')
print(f'Números ímpares digitados: {impares}')

'''

OU

numeros = list()
pares = list()
impares = list()
c = 0
while True:
    numeros.append(int(input('Digite um número: ')))
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
    else:
        impares.append(numeros[c])
    c += 1
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break
print(f'Todos os números digitados: {numeros}')
print(f'Números pares digitados: {pares}')
print(f'Números ímpares digitados: {impares}')

'''
