# APR, REP, REC

nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
media = (nota1 + nota2)/2

if media < 5.0:
    print('Sua média é {}. Você está REPROVADO!'.format(media))
elif 5.0 <= media <= 6.9:
    print('Sua média é {}. Você está em RECUPERAÇÃO!'.format(media))
else:
    print('Sua média é {}. Você está APROVADO!'.format(media))
