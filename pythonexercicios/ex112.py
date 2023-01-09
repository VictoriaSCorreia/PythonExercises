# EXCEÇÕES, FUNÇÕES

def leiaint(n): 
    while True:
        try: 
            num = int(input(n))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
        else:
           return num

def leiafloat(v):
    while True:
        try:
            valor = float(input(v))
        except (ValueError, TypeError):
            print('ERRO! Digite um número real válido.')
        else:
            return valor

    '''
    COM VÍRGULA  E SÓ ACEITA ENTRADA DE NÚMERO REAIS

    while True:
        valor = (input(v)).strip()
        cont1 = 0
        cont2 = 0
        for l in valor:
            if l.isnumeric():
                cont2 += 1
        for l in valor:
            if l in '.,':
                cont1 += 1
        try:
            teste = 5 / cont2
            teste = 5 / cont1 
        except:
            print('ERRO! Digite um número real válido.')
        else:
            return valor
    '''


valor = leiafloat(('Digite um número real: '))
print(f'Você acabou de digitar o número {valor}.')

num = leiaint(('Digite um número inteiro: '))
print(f'Você acabou de digitar o número {num}.')
