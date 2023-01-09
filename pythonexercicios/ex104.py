# FUNÇÕES, VALIDANDO NÚMERO INTEIRO

def leiaint(n):
    while True:
        teste = False
        for l in n:
            if l in '.,':
                teste = True
        if n.isnumeric():
            teste = True
        if teste:
            break    
        else:
            print('ERRO! Digite um número inteiro válido.')
        n = (input('Digite um número: '))
    return n

    
num = leiaint(input('Digite um número: '))
print(f'Você acabou de digitar o número {num}.')

'''
OU

def leiaint(n):
    alfabeto = list(map(chr, range(97, 123)))
    while True:
        teste = False
        for l in n:
            if l in alfabeto or l in '.,':
                teste = True
        if teste:
            print('ERRO! Digite um número inteiro válido.')
        else:
            break
        n = (input('Digite um número: '))
    return n

    
num = leiaint(input('Digite um número: '))
print(f'Você acabou de digitar o número {num}.')'''
