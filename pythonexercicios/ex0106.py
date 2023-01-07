# FUNÇÕES, SISTEMA INTERATIVO DE AJUDA

def ajuda():
    while True:
        resp = input('Função ou biblioteca > ').lower().strip()
        if resp != 'fim':
            print(f'{help(resp)}')
        else:
            break
    print(f'{"FIM!":^152}')
ajuda()
