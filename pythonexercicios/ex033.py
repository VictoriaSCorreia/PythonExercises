# MAIOR E MENOR NUMERO DE 3

n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))

# Vendo quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Vendo quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número é {:.0f}'.format(menor))
print('O maior número é {:.0f}'.format(maior))

# OU
"""
lista = [n1, n2, n3]
lista.sort()

print('Menor valor: {} \nMaior valor: {}'.format(lista[0], lista[2]))

"""
