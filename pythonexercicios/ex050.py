# Soma dos pares usando FOR
s = 0
print(' ')
for c in range(1, 7):
    num = int(input('Digite o {}° número inteiro: '.format(c)))
    if num % 2 == 0:
        s = s + num
print('A soma entre todos os números PARES é: {}'.format(s))
