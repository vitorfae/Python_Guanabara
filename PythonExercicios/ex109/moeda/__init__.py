def aumentar(valor, porcentagem, show = False):
    valor = valor * (1 + porcentagem / 100)
    if show == True:
        return moeda(valor)
    else:
        return valor

def diminuir(valor, porcentagem, show = False):
    porcentagem = porcentagem / 100
    valor = valor * (1 - porcentagem)
    if show == True:
        return moeda(valor)
    else:
        return valor

def dobro(valor, show = False):
    valor = valor * 2
    if show == True:
        return moeda(valor)
    else:
        return valor

def metade(valor, show = False):
    valor = valor / 2
    if show == True:
        return moeda(valor)
    else:
        return valor

def moeda(valor):
    return f'R${valor:.2f}'

#JEITO GUANABARA
'''
from os import replace


def aumentar(valor=0, porcentagem=0, show = False):
    resposta = valor + (1 * porcentagem / 100)
    return resposta if show is False else moeda(resposta)

def diminuir(valor, porcentagem, show = False):
    porcentagem = porcentagem / 100
    resposta = valor * (1 - porcentagem)
    return resposta if show is False else moeda(resposta)

def dobro(valor, show = False):
    resposta = valor * 2
    return resposta if show is False else moeda(resposta)

def metade(valor, show = False):
    resposta = valor / 2
    return resposta if show is False else moeda(resposta)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')'
'''