# IS (TRUE/FALSE)

n = (input('Digite algo: '))

print(type(n))
print('\nNúmero? {}\nPalavra? {}\nAlfanumérico? {}\n'.format(n.isnumeric(), n.isalpha(), n.isalnum()), end='')
print('Só minúsculo? {}\nSó maiúsculo? {}\nEspaço em branco? {}'.format(n.islower(), n.isupper(), n.isspace()))
