# FUNÇÕES, FICHA

def ficha(nome=str, gols=str):
    print('O jogador', end=' ')
    if nome.strip() == "":
        print(f'<desconhecidos>', end=' ')
    else:
        print(f'{nome}', end=' ')
    print('fez', end=' ')
    if gols == "" or gols.isnumeric() == False:
        print(f'0', end=' ')
    else:
        print(f'{gols}', end=' ')
    print('gols no campeonato.', end=' ')

nome = str(input('Nome do Jogador: '))
gols = str(input('N° de gols: '))
ficha(nome, gols)
