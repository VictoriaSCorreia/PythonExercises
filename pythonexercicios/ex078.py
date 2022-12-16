# LISTAS, MAIOR E MENOR VALOR

valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor da POSIÇÃO {c}: ')))
print(f'Você digitou os valores: {valores}')
print(f'\nO maior valor foi {max(valores)} nas posições:', end=' ')
for i, val in enumerate(valores):
    if max(valores) == val:
        print(f'{i}...', end=' ')
print(f'O menor valor foi {min(valores)} nas posições:', end=' ')
for i, val in enumerate(valores):
    if min(valores) == val:
        print(f'{i}...', end=' ')

'''
OU

for c in range(0, len(valores)):
    if max(valores) == valores[c]:
        print(f'{c}...', end=' ')
print(f'O menor valor foi {min(valores)} nas posições:', end=' ')
for c in range(0, len(valores)):
    if min(valores) == valores[c]:
        print(f'{c}...', end=' ')

'''

"""

OU 

valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {c}: ')))
for cont in valores:
    print(cont, end=' ')
print(f'\nO maior valor foi {max(valores)}, na posição {valores.index(max(valores))}')
print(f'O menor valor foi {min(valores)}, na posição {valores.index(min(valores))}')

"""
