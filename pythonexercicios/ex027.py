# Primeiro e último nome da string

nome = input('Digite seu nome completo: ').strip()

ultimo = nome.rfind(' ') + 1
primeiro = nome.split()

print('Seu primeiro e último nome são {} e {}'.format(primeiro[0], nome[ultimo:]))

"""
OU

nome = input('Digite seu nome completo: ').strip()
n = nome.split()
print('Seu primeiro e último nome são {} e {}'.format(n[0], n[len(n)-1]))

OU 

nome = input('Qual seu nome completo? ').strip().split()
print('Seu primeiro nome é {nome[0]}. \nSeu último nome é {nome[-1]}.')

"""
