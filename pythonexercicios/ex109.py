# MÓDULOS, MOEDAS 3

import moeda

valor = float(input('Digite o valor do produto: R$'))
print(f'O aumento do produto em 10%: {moeda.aumentar(valor, 10, True)}')
print(f'A diminuição do produto em 10%: {moeda.reduzir(valor, 13, True)}')
print(f'O dobro de {moeda.moeda(valor)} é: {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.moeda(valor)} é: {moeda.metade(valor, True)}')
