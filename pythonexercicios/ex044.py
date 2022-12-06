# OPÇÃO DE PAGAMENTO

val = float(input('Valor: '))
escolha = input('Deseja pagar utilizando dinheiro, cheque ou cartão? ').lower().strip()

if escolha == 'dinheiro' or escolha == 'cheque':
    valtotal = val - (val * 10 / 100)
    print('Você ganhou 10% de desconto! Valor atual: {:.2f}'.format(valtotal))

elif escolha == 'cartão' or escolha == 'cartao':

    escolha1 = input('À vista ou parcelado? ').lower().strip()

    if escolha1 == 'à vista' or escolha1 == 'a vista' or escolha1 == 'vista':
        valtotal = val - (val * 5 / 100)
        print('Você ganhou 5% de desconto! Valor atual: {:.2f}'.format(valtotal))

    elif escolha1 == 'parcelado':

        vezes = int(input('Em quantas vezes? '))

        if vezes <= 2:
            print('Sem juros. Valor total: {:.2f}'.format(val))
        else:
            valjuros = val + (val * 20 / 100)
            print('Você tem 20% de juros! Valor atual: {:.2f}'.format(valjuros))

    else:
        print('Escolha uma opção válida.')

else:
    print('Escolha uma opção válida.')
