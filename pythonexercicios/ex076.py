# TUPLAS, LISTA DE PREÇOS

produtos = ('Caneta', 2.35, 'Lápis', 2.00, 'Borracha', 2.25, 'Caderno', 25.99, 'Mochila', 68.50, 'Estojo', 29.90, 'Régua', 12.00, 'Marcador', 3.50, 'Apondador', 4.00)

print(f'\n{"="*50:>35}\n{"LISTAGEM DE PREÇOS":>34}\n{"="*50:>35}')
print(f'{"-"*50}')
for c in range(0, len(produtos)-1, 2):
    print(f'{produtos[c]}.............R$ {produtos[c+1]:.2f}')
print(f'{"-"*50}\n')