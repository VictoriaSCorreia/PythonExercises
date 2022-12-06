# Formatador de texto

nome = str(input('Digite seu nome completo: '))

print('\n')
print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))

dividido = nome.split()
junto = ''.join(dividido)

print('Seu nome tem {} letras ao todos'.format(len(junto)))
print('Seu primeiro nome "{}" tem {} letras'.format(dividido[0], len(dividido[0])))
