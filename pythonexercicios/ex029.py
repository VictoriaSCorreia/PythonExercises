# MULTA

vel = float(input('Km/h: '))

if vel > 80:
    print('Você recebeu uma multa de R${:.2f} por ultrapassar o limite de 80km/h.'
          .format((vel - 80) * 7.00))
print('Dirija com segurança!')
