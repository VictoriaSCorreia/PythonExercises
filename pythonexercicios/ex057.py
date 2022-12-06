# Validação de dados
sexo = input('Digite seu sexo: [M/F] ').strip().upper()[0]  # A primeira letra que vai contar
                                                            # Ex: Mulher <-- 'M'
while sexo not in 'MF':
    sexo = input('Informação inválida. Digite novamente: [M/F] ').strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
