# MAIOR E MENOR VALORES
resp = 'sim'
cont = soma = maior = menor = 0
while resp in 'sim':
    val = int(input('Digite um número: '))
    cont += 1
    soma += val
    if cont == 1:
        maior = val
        menor = val
    else:
        if val > maior:
            maior = val
        if val < menor:
            menor = val
    resp = input('Quer continuar? ').lower().strip()
print('A média dos valores foi {}'.format(soma/cont))
print('O menor valor foi {} e o maior foi {}'.format(menor, maior))
