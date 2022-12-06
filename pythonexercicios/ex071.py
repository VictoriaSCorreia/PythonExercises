# SACANDO DINHEIRO | COMANDO BREAK
total = cinquentaC = vinteC = dezC = umC = 0
saque = int(input('Qual valor será sacado? R$')) # 120
if saque >= 50:
    while True:
        total += 50  # 50 100 150
        if total > saque:
            break  # X
        cinquentaC += 1  # 1 2
    total -= 50  # 100
if saque - total >= 20:  # V
    while True:
        total += 20  # 120
        if total > saque:
            break
        vinteC += 1  # 1
    total -= 20
if saque - total >= 10:
    while True:
        total += 10
        if total > saque:
            break
        dezC += 1
    total -= 10
if saque - total >= 1:
    while True:
        total += 1
        if total > saque:
            break
        umC += 1
    total -= 1
print(f'Total de {cinquentaC} cédulas de R$50.')
print(f'Total de {vinteC} cédulas de R$20.')
print(f'Total de {dezC} cédulas de R$10.')
print(f'Total de {umC} cédulas de R$1.')


"""
saque = int(input('Qual valor será sacado? R$')) 
total = saque
cedula = 50
totced - 0
while True:
    if total >= cedula:
        total -= cedula 
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula})
        if cedula == 50:
            cedula = 20
        if cedula == 20:
            cedula = 10
        if cedula == 10:
            cedula = 1
        totced = 0            
        if total == 0:
            break
"""