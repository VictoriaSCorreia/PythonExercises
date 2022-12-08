# TUPLAS, CONTANDO VOGAIS
tupla = ('mercado', 'hospital', 'escola', 'academia', 'padaria')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} tem as vogais: ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
