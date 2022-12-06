# VÁRIOS VALORES (64) | COMANDO BREAK
cont = soma = 0
while True:
    num = int(input("Digite um número (999 faz parar): "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi {soma}')
