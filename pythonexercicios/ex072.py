# TUPLAS, NUM POR EXTENSO

tupla1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
tupla2 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número inteiro de 0 a 20: '))
while True:
    if num in tupla1:
        print(f'Você digitou o número {tupla2[num]}.')  #  OU tupla2[len(tupla2) - 1]
        break
    num = int(input('Digite um número inteiro de 0 a 20: '))

"""
OU

tupla = ('zero', 0, 'um', 1, 'dois', 2, 'três', 3, 'quatro', 4, 'cinco', 5, 'seis', 6, 'sete', 7, 'oito', 8, 'nove', 9, 'dez', 10, 'onze', 11, 'doze', 12, 'treze', 13, 'quatorze', 14, 'quinze', 15, 'dezesseis', 16, 'dezessete', 17, 'dezoito', 18, 'dezenove', 19, 'vinte', 20)

num = int(input('Digite um número inteiro de 0 a 20: '))
while True:
    if num in tupla:
        print(f'Você digitou o número {tupla[num+num]}.')
        break
    num = int(input('Digite um número inteiro de 0 a 20: '))

"""

