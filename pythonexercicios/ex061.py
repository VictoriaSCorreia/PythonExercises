# PROGRESSÃO ARITMÉTICA WHILE
t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
cont = 1
pa = t
print(' ' * 5, 'PROGRESSÃO ARITMÉTICA\nCom {} como 1° termo e {} como razão:\n'.format(t, r))
while cont <= 10:
    print(pa, end=' ')
    pa += r
    cont += 1

"""
OU 

t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
cont = 0
pa = t
print(' ' * 5, 'PROGRESSÃO ARITMÉTICA\nCom {} como 1° termo e {} como razão:\n'.format(t, r))
while cont <= t * 9:
    cont += t
    print(pa, end=' ')
    pa += r
"""