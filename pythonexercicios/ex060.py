# FATORIAL
# WHILE
n = int(input("Digite um número: "))
cont = n
fatorial = 1
print('{}! = {}'.format(n, n), end='')
while cont > 1:
    fatorial *= cont
    cont = cont - 1
    print(' x', cont, end='')
print(' =', fatorial)

"""

OU 
n = int(input("Digite um número: "))
cont = n
soma = 0
while cont > 1:
    cont = cont - 1
    if cont == n - 1:
        soma = n * cont
        print(n, "X", cont, "=", soma)
    else:
        print(soma, "X", cont, "= ", end='')
        soma = soma * cont
        print(soma)

# FOR

n = int(input("Digite um número: "))
cont = n
fatorial = 1
print('{}! = '.format(n), end='')
for cont in range(n, 0, -1):
    fatorial *= cont
    print('{} X'.format(cont) if cont > 1 else '{}'.format(cont), end=' ')
print('= {}'.format(fatorial))

OU

n = int(input("Digite um número: "))
cont = n
fatorial = 0
for cont in range(n-1, 0, -1):
    if cont == n - 1:
        fatorial = n * cont
        print(n, "X", cont, "=", fatorial)
    else:
        print(fatorial, "X", cont, "= ", end='')
        fatorial = fatorial * cont
        print(fatorial)
"""
        