# IMC
alt = float(input('Altura: '))
peso = float(input('Peso: '))
IMC = peso / (alt * alt)

if IMC < 18.5:
    print('Seu IMC é {:.1f}. Você está abaixo do peso.'.format(IMC))
elif 18.5 <= IMC < 25:
    print('Seu IMC é {:.1f}. Você está no peso ideal.'.format(IMC))
elif 25 <= IMC < 30:
    print('Seu IMC é {:.1f}. Você está com sobrepeso.'.format(IMC))
elif 30 <= IMC < 40:
    print('Seu IMC é {:.1f}. Você está com obesidade.'.format(IMC))
else:
    print('Seu IMC é {:.1f}. Você está com obesidadde mórbida.'.format(IMC))
