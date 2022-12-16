# LISTAS, EXTRAINDO DADOS

valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break
valores.sort(reverse= True)
print(f'\nForam digitados {len(valores)} valores.')
print(f'Em ordem decrescente: {valores}.')
if 5 in valores:
    print(f'O valor 5 foi encontrado {valores.count(5)} vezes na '
    'lista nas posições:', end= ' ')
    for c, num in enumerate(valores):
        if num == 5:
            print(c, end=' ')
else: 
    print('O valor 5 não foi encontrado na lista.')
