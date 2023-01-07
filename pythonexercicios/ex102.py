# FUNÇÕES, FATORIAL

def fatorial(num=1, show=False):
    """
    => Mostra o fatorial de um número
    :param num: Número a ser calculado
    :param show: (opcional) Mostra a conta
    :return: O valor do fatorial de num
    """
    fatorial = 1
    for c in range(num, 0, -1):
        fatorial *= c
        if show and c > 1:
            print(f'{c} x', end=' ')
        elif show and c == 1:
            print(f'{c} =', end=' ')
    return fatorial


print(fatorial(5))
help(fatorial)

'''
OU

def fatorial(num=1, show=False):
    """
    => Mostra o fatorial de um número
    :param num: Número a ser calculado
    :param show: (opcional) Mostra a conta
    :return: sem retorno
    """
    fatorial = 1
    for c in range(num, 0, -1):
        fatorial *= c
        if show and c > 1:
            print(f'{c} x', end=' ')
        elif show and c == 1:
            print(f'{c} =', end=' ')
    print(fatorial)

fatorial(5)
help(fatorial)
'''
