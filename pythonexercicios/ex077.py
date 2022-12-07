# TUPLAS, CONTANDO VOGAIS
tupla = ('mercado', 'hospital', 'escola', 'academia', 'padaria')

for c in tupla:
    print(f'\nNa palavra {c.upper()} tem as vogais: ', end=' ')
    for i in c:
        if i in 'aeiou':
            print(i, end=' ')
