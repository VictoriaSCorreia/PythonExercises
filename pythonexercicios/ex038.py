# MAIOR E MENOR

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro: '))

if num1 > num2:
    print('O número maior é o {} e o menor é {}.'.format(num1, num2))
elif num2 > num1:
    print('O número maior é o {} e o menor é {}.'.format(num2, num1))
else:
    print('Os números {} e {} são iguais.'.format(num1, num2))
