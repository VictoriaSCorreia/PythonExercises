# TUPLAS, ANÁLISE DE NÚMEROS

tupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')))
print(tupla)
print(f'O 9 aparece {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O 3 aparece na {tupla.index(3)+1}° prosição.')
else: 
    print('Não há número 3.')
print('São os pares:')
for c in tupla:
    if c % 2 == 0:
        print(c)
