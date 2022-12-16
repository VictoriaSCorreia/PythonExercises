# LISTAS, VALORES ÚNICOS

valores = list()
while True:
    teste = int(input('Digite um novo número: '))
    if teste not in valores:
        valores.append(teste)
        print('**** Valor adicionado.')
    else:
        print('**** Valor duplicado! NÃO adicionado.')
    resp = input('Quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break
valores.sort()
print(f'\nValores digitados: {valores}')  #  OU sorted(valores)
