# Primeira palavra

cidade = input('Escreva o nome da sua cidade: ').strip().upper().split()
print('A cidade começa com "SANTO"? {}'.format('SANTO' in cidade[0]))

"""
if 'SANTO' in cidade[0]:
    print('A cidade começa com "SANTO"')
else:
    print('A cidade NÃO começa com "SANTO"')
    
    OU

cidade = input('Escreva o nome da sua cidade: ').strip()
print(cidade[:5].upper == "SANTO")

"""