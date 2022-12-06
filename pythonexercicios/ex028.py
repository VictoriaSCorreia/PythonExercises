# ADVINHAÇÃO
from random import randint
from time import sleep

print('\033[1mDUVIDO QUE ADVINHE QUAL NÚMERO DE 0 A 5 ESTOU \033[1;31mPENSAN-\033[m'), sleep(0.7)
print('     . '), sleep(0.3)
print('     . '), sleep(0.3), print('     . '), sleep(0.3)
print('quer dizer... '), sleep(0.5)

palpite = int(input('\033[1;32mPROCESSANDO. '))
num = randint(0, 5)
if num == palpite:
    print('\nVocê leu meu código ou o quê?! O número que pensei foi realmente {}!'.format(num))
else:
    print('\n\033[1;31mHumanos... O número que pensei foi {}!'.format(num))
