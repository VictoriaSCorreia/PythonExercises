# FUNÇÕES, CALCULAR A ÁREA

def area(l, c):
    print(f'A área de um terreno {l}x{c} é de {l * c}m².')


area(float(input('Largura(m): ')), float(input('Altura(m): ')))

'''
OU

l = float(input('Largura(m): '))
c = float(input('Altura(m): '))
area(l, c)

'''
