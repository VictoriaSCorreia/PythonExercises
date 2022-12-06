# EMPRÉSTIMO

valcasa = float(input('Qual é o valor da casa que deseja? R$'))
salario = float(input('Qual é o seu salário mensal? R$'))
anos = int(input('Em quantos anos deseja pagar? '))

totmeses = anos * 12
parcelas = valcasa/totmeses
porc = salario * 30 / 100

print('Sua prestação mensal é de R${:.2f}.'.format(parcelas))
if parcelas <= porc:
    print('EMPRÉSTIMO APROVADO.')
else:
    print('EMPRÉSTIMO NEGADO. ')
