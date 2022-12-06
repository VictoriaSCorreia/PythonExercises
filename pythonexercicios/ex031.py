# Calculando preço de viagem

km = float(input('Qual a distância(Km) da sua viagem? '))

if km <= 200:
    valor = 0.50 * km
else:
    valor = 0.45 * km
print('Sua viagem custará R${:.2f}.'.format(valor))
