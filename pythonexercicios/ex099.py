# FUNÇÕES, NÚMERO MAIOR

from time import sleep
def maior(*numeros):
    c = 0
    for v in numeros:
        print(f'{v}', end=' ', flush=True)
        sleep(0.5)
        c += 1
        if numeros.index(v) == 0:
            maior = v
        else:
            if v > maior:
                maior = v
    print()
    print(f'Foram informados {c} valores.')
    print(f'O maior valor foi {maior}.')


maior(1, 4, 2, 3, -5, -6, -5)

'''
OU 

def maior(*numeros):
    print(f'Foram informados {len(numeros)} valores.')
    print(f'O maior valor foi {max(numeros)}.')

maior(1, 5, 2, 7, 9, 3, 15)'''
