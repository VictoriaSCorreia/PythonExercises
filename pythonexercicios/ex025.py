# Achar palavra dentro da string

nome = input('Digite seu nome completo: ').upper()

if 'SILVA' in nome:
    print('Você tem SILVA no nome? \033[1;32m{}'.format('SILVA' in nome))
else:
    print('Você tem SILVA no nome? \033[1;31m{}'.format('SILVA' in nome))
