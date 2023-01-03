# DICIONÁRIOS, CADASTRO DE TRABALHADOR

from datetime import date
pessoa = {'Nome': input('Nome: ')}
nasc = int(input('Ano de nascimento: '))
pessoa['Idade'] = date.today().year - nasc
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salario'] = float(input('Salário R$:'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + (35 - (date.today().year - pessoa['Contratação']))
for k, v in pessoa.items():
    print(f'  => {k.upper()} tem o valor {v}.')
