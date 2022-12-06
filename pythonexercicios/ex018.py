# SEN, COS, TANG

from math import cos, sin, tan, radians

ang = float(input('Digite o ângulo: '))
coss = cos(radians(ang))
seno = sin(radians(ang))
tang = tan(radians(ang))

print('\nO ângulo de {} tem:\n\nSENO {:.2f}'
      '\nCOSSENO {:.2f}\nTANGENTE {:.2f}'.format(ang, seno, coss, tang))
