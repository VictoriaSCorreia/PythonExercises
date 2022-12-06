# PRODUTOS | COMANDO BREAK
total = totalmil = cont = menor = 0
produtomenor = str
while True:
    produto = str(input('Produto: '))
    preco = float(input('Valor: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totalmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        produtomenor = produto
    while True:
        resp = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
        if resp in 'sn':
            break
    if resp == 'n':
        break
print(f'Total: R${total:.2f}\n{totalmil} produtos custam mais de R$1000\n'
      f'{produtomenor} é o produto mais barato e custa R${menor:.2f}')
