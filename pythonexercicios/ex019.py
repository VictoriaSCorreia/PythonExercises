# Sorteando um aluno

from fRandomm import choice

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a3]

sorteado = choice(lista)

print('O aluno sorteado foi {}'.format(sorteado))

