# LISTAS, ORDENANDO SEM O SORT()

valores = list()
for c in range(0, 5):
    teste = int(input('Digite um valor: '))
    if c == 0 or teste >= max(valores):    # ou valores[len(valores)-1], valores[-1]
        valores.append(teste)
        print(f'Valor adicionado no final da lista.')
    else:
        for cont in range(0, len(valores)):
            if teste <= valores[cont]:
                valores.insert(cont, teste)
                print(f'Valor adicionado na {cont}° posição da lista.')
                break        
print(f'Valores em ordem: {valores}')

'''

valores = list()
for c in range(0, 5):
    teste = int(input('Digite um valor: '))
    if c == 0 or teste >= max(valores):    # ou valores[len(valores)-1], valores[-1]
        valores.append(teste)
        print(f'Valor adicionado no final da lista.')
    else:
        if teste <= min(valores): 
            valores.insert(0, teste)
            print(f'Valor adicionado no início da lista.')
        else:    
            for cont in range(0, len(valores)):
                if teste >= valores[cont] and teste < valores[cont + 1]:
                    valores.insert(cont + 1, teste)
                    print(f'Valor adicionado na {cont + 1}° posição da lista.')
                    break        
print(f'Valores em ordem: {valores}')

'''