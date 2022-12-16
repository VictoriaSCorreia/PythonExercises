# VALIDANDO UMA EXPRESSÃO

exp = input('Digite uma expressão matemática: ').strip().split()
if exp.count('(') == exp.count(')'):
    print('Sua expressão está correta!')
else: 
    print('Sua expressão está incorreta!')

'''
OU 

exp = input('Digite uma expressão matemática: ')
pilha = list()
for letra in exp:
    if letra == '(':
        pilha.append('(')
    elif letra == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')

'''
