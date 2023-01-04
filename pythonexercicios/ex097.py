# FUNÇÕES, PRINT ELABORADO

def escreva(frase):
    tamanho = len(frase) + 4
    print('=' * (tamanho))
    print(f'  {frase}')
    print('=' * (tamanho))

'''
OU

tamanho = len(frase)
    print('=' * (tamanho + 2))
    print(f'{"" * int(tamanho / 2 )}', f'{frase}')
    print('=' * (tamanho + 2))
'''
escreva('Hello, world!')
