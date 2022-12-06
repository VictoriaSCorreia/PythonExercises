# ANALISADOR COMPLETO
soma = 0
maioridade = 0
maiornome = ''
totmulher = 0
for c in range(1, 5):
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').strip().lower()
    soma = soma + idade
    if sexo == 'm' or sexo == 'masculino' or sexo == 'homem':
        if idade > maioridade:
            maioridade = idade
            maiornome = nome
    elif sexo == 'f' or sexo == 'feminino' or sexo == 'mulher' and idade < 20:
        totmulher = totmulher + 1
mediaidade = soma / 4
print('A média de idade do grupo é {}'.format(mediaidade))
print('O nome do homem mais velho é {}, com {} anos'.format(maiornome, maioridade))
print('{} mulheres têm menos de 20 anos'.format(totmulher))


"""
OU

soma1 = 0
soma2 = 0
maior1 = 0
contador = 0
nome1 = 0
for c in range(1, 5):
    sexo = input('Sexo: ').lower().strip()
    if sexo == 'homem' or sexo == 'masculino' or sexo == 'm':
        idade = int(input('Idade: '))
        soma1 = soma1 + idade
        nome = input('Nome: ')
        if idade > maior1:
            maior1 = idade
            nome1 = nome
    elif sexo == 'mulher' or sexo == 'feminino' or sexo == 'f':
        idade = int(input('Idade: '))
        soma2 = soma2 + idade
        if idade < 20:
            contador = contador + 1
        nome = input('Nome: ')
    else:
        print('Digite corretamente.')
print('O nome do homem mais velho é {}'.format(nome1))
print('{} mulheres têm menos de 20 anos'.format(contador))
print('A média de idade do grupo é {}'.format((soma1 + soma2)/4))
"""
