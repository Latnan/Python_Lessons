import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Erro!')
else:
    print('Acessado com sucesso.')
    print(site.read())
