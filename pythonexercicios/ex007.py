# MÉDIA

nome = input('Insira o nome do aluno: ')
nota1 = float(input('\nInsira a primeira nota de {}: '.format(nome)))
nota2 = float(input('Insira a segunda nota: '))
media = float((nota1 + nota2)/2)

print('MÉDIA: {:.1f}'.format(media))
