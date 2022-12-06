# Soma ímpares múltiplos de três usando FOR
s = 0
v = 0
for a in range(3, 500, +3):
    if a % 2 == 1:
        s = a + s
        v = v + 1
print('A soma dos {} valores é {}'.format(v, s))
