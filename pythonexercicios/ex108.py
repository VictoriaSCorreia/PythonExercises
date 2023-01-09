# MÓDULOS, MOEDAS 2

import moeda

valor = float(input('Digite o valor do produto: R$'))
print(f'O aumento do produto em 10%: {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'A diminuição do produto em 10%: {moeda.moeda(moeda.reduzir(valor, 13))}')
print(f'O dobro de {moeda.moeda(valor)} é: {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é: {moeda.moeda(moeda.metade(valor))}')
