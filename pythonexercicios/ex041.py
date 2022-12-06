# CLASSES DO JOGADOR
from datetime import date
nasc = int(input('Ano de Nascimento: '))
anos = date.today().year - nasc

if anos <= 9:
    print('   Sua idade é de {} anos\n   JOGADOR MIRIM'.format(anos))
elif 9 < anos <= 14:
    print('   Sua idade é de {} anos\n  JOGADOR INFANTIL'.format(anos))
elif 14 < anos <= 19:
    print('   Sua idade é de {} anos\n   JOGADOR JUNIOR'.format(anos))
elif 19 < anos <= 20:
    print('   Sua idade é de {} anos\n   JOGADOR SÊNIOR'.format(anos))
else:
    print('   Sua idade é de {} anos\n   JOGADOR MASTER'.format(anos))
