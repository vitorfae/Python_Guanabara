import requests

def verificarSiteAcessivel(url):
    try:
        resposta = requests.get(url)
    except:
        print('\033[031mO site pudim não está acessível no momento.\033[m')
    else:
        print('\033[032mConsegui acessar o site do pudim com sucesso!\033[m')

verificarSiteAcessivel('https://www.pudim.com.br/')


#JEITO GUANABARA
'''import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print('\033[031mO site pudim não está acessível no momento.\033[m')
else:
    print('\033[032mConsegui acessar o site do pudim com sucesso!\033[m')
    print(site.read()) #-> Pega o conteúdo HTML do site'''