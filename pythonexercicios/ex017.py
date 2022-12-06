# HIPOTENUSA

from math import hypot

ops = float(input('Cateto oposto: '))
adj = float(input('Cateto adjacente: '))

print('O comprimento da hipotenusa é: {:.2f}'.format(hypot(ops, adj)))
