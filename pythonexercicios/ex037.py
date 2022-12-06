# BI, HEX E OCT

num = int(input('Você quer converter qual número? '))
escolha = input('Converter em: \033[31m(1)\033[m Binário | \033[35m(2)\033[m '
                'Octadecimal | \033[33m(3)\033[m Hexadecinal.  ')

if escolha == '1':
    print(bin(num)[2:])

elif escolha == '2':
    print(oct(num)[2:])

elif escolha == '3':
    print(hex(num)[2:])

else:
    print('Escolha um número válido.')
