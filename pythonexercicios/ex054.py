# Grupo da maioridade

from datetime import date
contador = 0
for c in range(1, 8):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - nasc
    if idade < 21:
        contador = contador + 1
print('{} pessoas atingiram a maioridade'.format(7-contador))
print('{} pessoas são menores de idade'.format(contador))
