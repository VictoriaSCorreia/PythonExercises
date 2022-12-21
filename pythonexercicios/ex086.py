# LISTAS COMPOSTAS, MATRIZ

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}] '))
print('\n')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('\n')

'''

OU

matriz = []
linha0 = []
linha1 = []
linha2 = []
for l in range(0, 3):
    for c in range(0, 3):
        teste = int(input(f'Digite um número para [{l}, {c}] '))
        if l == 0:
            linha0.append(teste) 
        elif l == 1:
            linha1.append(teste)
        elif l == 2: 
            linha2.append(teste)
print('\n')
matriz.append(linha0[:])
matriz.append(linha1[:])
matriz.append(linha2[:])
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end=' ')
    print()       
print('\n')


OU

matriz = []
linha0 = []
linha1 = []
linha2 = []
for l in range(0, 3):
    for c in range(0, 3):
        teste = int(input(f'Digite um número para [{l}, {c}] '))
        if l == 0:
            linha0.append(teste) 
        elif l == 1:
            linha1.append(teste)
        elif l == 2: 
            linha2.append(teste)
print('\n')
matriz.append(linha0[:])
matriz.append(linha1[:])
matriz.append(linha2[:])
for l in range(0, 3):
    for c in range(0, 3):
        if l == 0:
            if c < 2:
                print(f'[ {matriz[l][c]:^5} ]', end=' ')
            else:
                print(f'[ {matriz[l][c]:^5} ]')
        elif l == 1:
            if c < 2:
                print(f'[ {matriz[l][c]:^5} ]', end=' ')
            else:
                print(f'[ {matriz[l][c]:^5} ]')
        elif l == 2:
            if c < 2:
                print(f'[ {matriz[l][c]:^5} ]', end=' ')
            else:
                print(f'[ {matriz[l][c]:^5} ]')
print('\n')
'''
