# FUNÇÕES, CONTADOR

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 25)
    print(f'CONTAGEM de {inicio} até {fim} de {passo} e {passo}')
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
    else:
        for c in range(inicio, fim - 1 , passo - (passo + passo)):
            print(c, end=' ')
    print()
    print('-=' * 25)


contador(1, 10, 1)
contador(10, 0, 2)
print(f'Agora é a sua vez de personalizar a contagem! ')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

'''
OU

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 25)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio > fim:  
        fim = fim - passo
        passo = passo - passo * 2
    for c in range(inicio, fim + 1, passo):
        print(c, end='... ')
    print('FIM!')
    print('-=' * 25)

'''
