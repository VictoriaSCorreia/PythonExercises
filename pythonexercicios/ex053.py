# PALÍNDROMO
frase = str(input('Digite alguma coisa: ')).strip().lower()
lista = frase.split()
frase = ''.join(lista)
tamanho = len(frase) - 1
potato = 0
for c in range(0, tamanho + 1):
    if frase[c] == frase[tamanho - c]:
        potato = potato + 1
if potato == len(frase):
    print('Você escreveu um palíndromo.')
else:
    print('Você escreveu algo normal.')

"""
OU
frase = str(input('Digite alguma coisa: ')).strip().lower()
lista = frase.split()
frase = ''.join(lista)
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[letra]
if inverso == frase:
    print('Você escreveu um palíndromo.')
else:
    print('Você escreveu algo normal.')
    
OU 
frase = str(input('Digite alguma coisa: ')).strip().lower()
lista = frase.split()
frase = ''.join(lista)
inverso = frase[::-1]
if inverso == frase:
    print('Você escreveu um palíndromo.')
else:
    print('Você escreveu algo normal.')

"""
