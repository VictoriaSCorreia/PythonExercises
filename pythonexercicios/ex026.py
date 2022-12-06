# Primeira e última letra na string

frase = input('Digite qualquer coisa: ').strip().lower()

print('A letra \033[4ma\033[m aparece {} vezes.'.format(frase.count('a')))
print('A primeira letra \033[4ma\033[m aparece na {}° prosição.'.format(frase.find('a')+1))
print('A última letra \033[4ma\033[m aparece na {}° posição.'.format(frase.rfind('a')+1))
