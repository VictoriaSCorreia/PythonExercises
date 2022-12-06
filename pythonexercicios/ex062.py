# PROGRESSÃO ARITMÉTICA WHILE 2.0

# ESSA VERSÃO PERGUNTA QUANTOS TERMOS VAI TER NA PA
t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
resp = int(input("Quantos termos você quer na PA? "))
cont = 1
pa = t
print('\n', ' ' * 16, 'PROGRESSÃO ARITMÉTICA\nCom \033[34m{}\033[m como 1° termo, '
                      '\033[34m{}\033[m como razão e \033[33m{}\033[m '
                      'como quantidade de termos:'.format(t, r, resp))
while cont <= resp:
    print(pa, end=' ')
    pa += r
    cont += 1

"""
# ESSA VERSÃO, APÓS OS 10 TERMOS INICIAIS, PERGUNTA QUANTOS MAIS IRÁ ADICIONAR

t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
cont = 1
pa = t
print(' ' * 8, 'PROGRESSÃO ARITMÉTICA de: \n\033[32m10\033[m termos! '
               'Com \033[34m{}\033[m como 1° termo e \033[34m{}\033[m como razão:'.format(t, r))
while cont <= 10:
    print(pa, end=' ')
    pa += r
    cont += 1
escolha = input('\n\nVocê quer adicionar mais termos? [Sim/Não] ').lower().strip()
if escolha in 'sim':
    resp = int(input('Digite quantos termos: '))
    cont = 1
    pa = t
    print('\nPROGRESSÃO ARITMÉTICA de:\n\033[32m{}\033[m Termos!'.format(resp + 10))
    while cont <= (10 + resp):
        print(pa, end=' ')
        pa += r
        cont += 1


# ESSA VERSÃO, APÓS OS 10 TERMOS INICIANTES, PERGUNTA QUANTOS MAIS IRÁ ADICIONAR E OS ADICIONA SEPARADAMENTE

t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
cont = 1
pa = t
escolha = 'sim'
print(' ' * 8, 'PROGRESSÃO ARITMÉTICA de: \n\033[32m10\033[m termos! '
               'Com \033[34m{}\033[m como 1° termo e \033[34m{}\033[m como razão:'.format(t, r))
while cont <= 10:
    print(pa, end=' -> ')
    pa += r
    cont += 1
cont -= 1
while escolha in 'sim':
    escolha = input('\n\nVocê quer adicionar mais termos? [Sim/Não] ').lower().strip()
    resp = int(input('Digite quantos termos: '))
    print('\nPROGRESSÃO ARITMÉTICA de:\n\033[32m{}\033[m Termos!'.format(resp + cont))
    cont1 = cont - 1
    while cont <= cont1 + resp:
        cont += 1
        print(pa, end=' -> ')
        pa += r


# ESSA VERSÃO, APÓS OS 10 TERMOS INICIAIS, PERGUNTA DE 1 EM 1 SE QUER ADICIONAR MAIS 1

t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
cont = 0
escolha = 'sim'
pa = t + r

print(' ' * 5, 'PROGRESSÃO ARITMÉTICA\nCom {} como 1° termo e {} como razão:\n'.format(t, r))
print(t, end=' ')
while cont != t * 9:
    cont += t
    print(pa, end=' ')
    pa = pa + r
while escolha == 'sim':
    escolha = input('\nVocê quer adicionar mais um termo? [Sim/Não] ').lower().strip()
    if escolha == 'sim':
        print(pa, end=' ')
        pa = pa + r
print(' ')

"""
