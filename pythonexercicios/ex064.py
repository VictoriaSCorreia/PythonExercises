# VÁRIOS VALORES 2.0
soma = num = 0
cont = -1
while num != 999:
    cont += 1
    soma += num
    num = (int(input('Digite um número: ')))
print('\nVocê digitou {} números.'.format(cont))
print('A soma dos números foi: {}.'.format(soma))
