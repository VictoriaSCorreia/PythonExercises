# CARRO ALUGADO

dias = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos quilômetros foram rodados? '))
custo = 60 * dias + 0.15 * km

print('Custo: {:.2f}R$'.format(custo))
