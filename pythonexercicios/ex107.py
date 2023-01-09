# MÓDULOS, MOEDAS 1

import moeda

valor = float(input('Digite o valor do produto: R$'))
print(f'O aumento do produto em 10%: R${moeda.aumentar(valor, 10)}')
print(f'A diminuição do produto em 10%: R${moeda.reduzir(valor, 13)}')
print(f'O dobro de {valor} é: R${moeda.dobro(valor)}')
print(f'A metade de {valor} é: R${moeda.metade(valor)}')
