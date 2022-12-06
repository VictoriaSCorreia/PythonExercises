# TABUADA USANDO FOR
n = int(input('Digite um número: '))
for c in range(0, 11):
    tot = n * c
    if c % 2 == 0:
        c = '\033[7;30m{}\033[m'.format(c)
    else:
        c = '\033[7m{}\033[m'.format(c)
    print('{} x {} = {}'.format(n, c, tot))
