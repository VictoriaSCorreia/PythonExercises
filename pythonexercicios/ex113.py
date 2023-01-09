# EXCEÇÕES, ACESSO A UM SITE

import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print(f'Não foi possível acessar o site do pudim.')
else:
        print(f'Site do pudim acessado com sucesso!')
