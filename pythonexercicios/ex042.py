# EQUI, ESCA, ISÓSC

lA = float(input('Digite o primeiro lado: '))
lB = float(input('Digite o segundo lado: '))
lC = float(input('Digite o terceiro lado: '))

if lA > 0 and lB > 0 and lC > 0:
    if lA + lB > lC and lB + lC > lA and lA + lC > lB:
        if lA != lB and lB != lC and lA != lC:
            print('TRIÂNGULO ESCALENO!')
        elif lC == lA == lB:
            print('TRIÂNGULO EQUILÁTERO!')
        else:
            print('TRIÂNGULO ISÓSCELES!')
    else:
        print('Não é um triângulo!')
else:
    print('Tendo ao menor um lado menor que 0, não é um triângulo!')
