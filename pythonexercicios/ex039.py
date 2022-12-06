from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nasc

if idade < 18:
    print('Sua idade é {}. Você pode se alistar em até {} anos.'.format(idade, 18 - idade))
elif idade > 18:
    print('Sua idade é {}. Já passaram {} anos desde a idade obrigatória.'.format(idade, idade - 18))
else:
    print('Sua idade é {}. Já está no tempo de seu alistamento.'.format(idade))
