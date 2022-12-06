# NÚMEROS PRIMOS
cont = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        cont = cont + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if cont == 2:
    print('\033[m\nO número {} é primo.'.format(n))
else:
    print('\033[m\nO número {} não é primo.'.format(n))

"""
OU

cont = 0
n = int(input('Digite um número: '))
if n <= 2:
    print('O número {} não é primo.'.format(n))
else:
    for c in range(2, n):
        if n % c == 0:
            cont = cont + 1
if cont > 0:
    print('O número {} não é primo.'.format(n))
else:
    print('O número {} é primo.'.format(n))
"""