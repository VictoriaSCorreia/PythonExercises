# LISTAS COMPOSTAS, PARES E ÍMPARES

numeros = [[], []]
teste = 0
for c in range(1, 8):
    teste = int(input(f'Digite o {c}° número: '))
    if teste % 2 == 0:
            numeros[0].append(teste)     
    else:
            numeros[1].append(teste)
numeros[0].sort()
numeros[1].sort()
print(f'Valores PARES: {numeros[0]}\nValores ÍMPARES: {numeros[1]}')

'''

OU 

numeros = [[], []]
teste = 0
for c in range(1, 8):
    teste = int(input(f'Digite o {c}° número: '))
    if teste % 2 == 0:
        if len(numeros[0]) == 0 or teste >= max(numeros[0]):
            numeros[0].append(teste)
        else:
            for cont in range(0, len(numeros[0])):
                if teste <= numeros[0][cont]:
                    numeros[0].insert(cont, teste)
                    break        
    else:
        if len(numeros[1]) == 0 or teste >= max(numeros[1]):
            numeros[1].append(teste)
        else:
            for cont in range(0, len(numeros[1])):
                if teste <= numeros[1][cont]:
                    numeros[1].insert(cont, teste)
                    break
print(f'Valores PARES: {numeros[0]}\nValores ÍMPARES: {numeros[1]}')


OU

pares = []
impares = []
numeros = []
for c in range(1, 8):
    teste = int(input(f'Digite o {c}° número: '))
    if teste % 2 == 0:
        if len(pares) == 0 or teste >= max(pares):
            pares.append(teste)
        else:
            for cont in range(0, len(pares)):
                if teste <= pares[cont]:
                    pares.insert(cont, teste)
                    break        
    else:
        if len(impares) == 0 or teste >= max(impares):
            impares.append(teste)
        else:
            for cont in range(0, len(impares)):
                if teste <= impares[cont]:
                    impares.insert(cont, teste)
                    break
numeros.append(pares[:])
numeros.append(impares[:])
print(f'Valores PARES: {numeros[0]}\nValores ÍMPARES: {numeros[1]}')
'''
