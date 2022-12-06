# TABUADA | COMANDO BREAK
valor = 0
while True:
    cont = 0
    valor = int(input("Quer ver a tabuada de qual valor? "))
    if valor < 0:
        break
    while cont < 10:
        cont += 1
        print(f'{valor} x {cont} = {valor * cont}')
print('TABUADA ENCERRADA.')

"""

valor = 0
while True:
    valor = int(input("Quer ver a tabuada de qual valor? "))
    if valor < 0:
        break
    for c in range(1, 11):
        print(f'{valor} x {cont} = {valor * cont}')
print('TABUADA ENCERRADA.')

"""