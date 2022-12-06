# ÁREA E LITROS

larg = float(input('Digite a largura da parede (metros): '))
alt = float(input('Digite a altura da parede (metros): '))
area = larg * alt

print('A área da sua parede é de {}m2.\nSerão necessários {}L de tinta para pintá-la.'.format(area, area/2))
