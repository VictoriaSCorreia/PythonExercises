# LISTAS COMPOSTAS, MATRIZ 2.0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}] '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
print('\n')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('\n')
somacoluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'\nA SOMA de todos os números PARES é {somapar}')
print(f'A SOMA dos números da TERCEIRA coluna é {somacoluna3}')
print(f'O maior valor da SEGUNDA linha é {max(matriz[1])}')

'''

OU

matriz = []
linha0 = []
linha1 = []
linha2 = []
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        teste = int(input(f'Digite um número para [{l}, {c}] '))
        if l == 0:
            linha0.append(teste) 
        elif l == 1:
            linha1.append(teste)
        elif l == 2: 
            linha2.append(teste)
        if teste % 2 == 0:
            soma += teste
print('\n')
matriz.append(linha0[:])
matriz.append(linha1[:])
matriz.append(linha2[:])
for l in range(0, 3):
    for c in range(0, 3):
        if l == 0:
            if c < 2:
                print(f'[ {matriz[l][c]} ]', end=' ')
            else:
                print(f'[ {matriz[l][c]} ]')
        elif l == 1:
            if c < 2:
                print(f'[ {matriz[l][c]} ]', end=' ')
            else:
                print(f'[ {matriz[l][c]} ]')
        elif l == 2:
            if c < 2:
                print(f'[ {matriz[l][c]} ]', end=' ')
            else:
                print(f'[ {matriz[l][c]} ]')
somacoluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'\nA SOMA de todos os números PARES é {soma}')
print(f'A SOMA dos números da TERCEIRA coluna é {somacoluna3}')
print(f'O maior valor da SEGUNDA linha é {max(matriz[1])}')


OU

matriz = []
linha0 = []
linha1 = []
linha2 = []
soma = somacoluna3 = maiorlinha2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        teste = int(input(f'Digite um número para [{l}, {c}] '))
        if l == 0:
            linha0.append(teste) 
        elif l == 1:
            linha1.append(teste)
            if c == 0:
                maiorlinha2 = teste
            else:
                if teste > maiorlinha2:
                    maiorlinha2 = teste
        elif l == 2: 
            linha2.append(teste)
        if teste % 2 == 0:
            soma += teste
        if c == 2:
            somacoluna3 += teste
print('\n')
matriz.append(linha0[:])
matriz.append(linha1[:])
matriz.append(linha2[:])
for l in range(0, 3):
    for c in range(0, 3):
        if l == 0:
            if c < 2:
                print(f'[ {matriz[l][c]} ]', end=' ')
            else:
                print(f'[ {matriz[l][c]} ]')
        elif l == 1:
            if c < 2:
                print(f'[ {matriz[l][c]} ]', end=' ')
            else:
                print(f'[ {matriz[l][c]} ]')
        elif l == 2:
            if c < 2:
                print(f'[ {matriz[l][c]} ]', end=' ')
            else:
                print(f'[ {matriz[l][c]} ]')
print(f'\nA SOMA de todos os números PARES é {soma}')
print(f'A SOMA dos números da TERCEIRA coluna é {somacoluna3}')
print(f'O maior valor da SEGUNDA linha é {maiorlinha2}')
'''
