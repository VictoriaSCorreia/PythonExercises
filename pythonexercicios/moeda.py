# AULA 22

def aumentar(n, p, f=False):
    """
    :param n: Valor a ser calculado
    :param p: Porcentagem de aumento do valor
    :param f: (opicional) Formatar aumento como moeda
    :return: aumento

    """
    aumento = n + (n * p / 100)
    if f:
        aumento = f'R${aumento}'.replace('.', ',')
    return aumento
    #return aumento if f is False else moeda(aumento)

def reduzir(n, p, f=False):
    """
    :param n: Valor a ser calculado
    :param p: Porcentagem de redução do valor
    :param f: (opicional) Formatar redução como moeda
    :return: redução
    
    """
    redução = n - (n * p / 100)
    if f:
        redução = f'R${redução}'.replace('.', ',')
    return redução

def dobro(n, f=False):
    """
    :param n: Valor a ser dobrado
    :param f: (opicional) Formatar dobro como moeda
    :return: dobro
    
    """
    dobro = n * 2
    if f:
        dobro = f'R${dobro}'.replace('.', ',')
    return dobro

def metade(n, f=False):
    """
    :param n: Valor a ser dividido
    :param f: (opicional) Formatar metade como moeda
    :return: metade
    
    """
    metade = n / 2
    if f:
        metade = f'R${metade}'.replace('.', ',')
    return metade

def moeda(n):
    """
    :param n: Valor a ser formatado
    :return: n

    """
    n = f'R${n}'.replace('.', ',')
    return n


def resumo(n, aum, red):
    """
    :param n: Valor a ser calculado
    :param am: Porcentagem de aumento do valor
    :param red: Porcentagem de redução do valor
    :return: sem retorno

    Chama os métodos: moeda; dobro; metade; aumentar; reduzir
    
    """
    import moeda
    print('-=' * 14)
    print(f'{"RESUMO DO VALOR":>21}')
    print('-=' * 14)
    print(f'Preço analisado: {moeda.moeda(n)}')
    print(f'Dobro do Preço: {moeda.dobro(n, True)}')
    print(f'Metade do Preço: {moeda.metade(n, True)}')
    print(f'Aumento de {aum}%: {moeda.aumentar(n, aum, True)}')
    print(f'Redução de {red}%: {moeda.reduzir(n, red, True)}')

def leiaDinheiro(n):
    """ 
    :param n: Valor a ser conferido
    :return: n
    
    - Testa se n é um valor monetário

    """

    teste = False
    while not teste:
        entrada = str(input(n)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! "{entrada}" é um preço inválido.')
        else:
            teste = True
            return float(entrada)
    
    '''
    OU
    
    teste = False
    while True:
        entrada = str(input(n)).replace(',', '.')
        for l in entrada:
            if l in '.,':
                teste = True
        if entrada.isnumeric():
            teste = True
        if teste:
            break    
        else:
            print(f'ERRO! "{entrada}" é um preço inválido.')
    return float(entrada)
    
    '''
