# CONTAGEM REGRESSIVA USANDO FOR

from time import sleep
import emoji

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!\n', emoji.emojize(':fireworks:' * 7, language='alias'))
