# MENU DE OPÇÕES
op = 0
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
while op != 5:
    if op == 4:
        n1 = int(input("\nDigite o 1° número: "))
        n2 = int(input("Digite o 2° número: "))
    print('''    [1] Somar
    [2] Multiplicar
    [3] O número maior
    [4] Digitar novos números
    [5] Sair do programa  ''', end='')
    op = int(input(' '))
    if op == 1:
        print("\nA soma entre {} + {} é: {}".format(n1, n2, n1 + n2))
    elif op == 2:
        print("\nA multiplicação entre {} X {} é: {}".format(n1, n2, n1 * n2))
    elif op == 3:
        print("\nO maior número entre {} e {} é: ".format(n1, n2), end='')
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif op > 5 or op < 1:
        print("Digite uma opção válida.")
