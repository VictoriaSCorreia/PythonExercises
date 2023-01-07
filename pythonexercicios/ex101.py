# FUNÇÕES, VOTAÇÃO

def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Você possui {idade} anos.', end=' ')
    if idade < 16:
        print('VOTO NEGADO.')
    elif idade > 65:
        print('VOTO OPCIONAL.')
    else:
        print('VOTO OBRIGATÓRIO.')


voto(int(input('Data de nascimento: ')))
