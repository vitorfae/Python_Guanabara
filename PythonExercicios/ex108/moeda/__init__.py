from os import replace


def aumentar(valor, porcentagem):
    valor = valor + (1 * porcentagem / 100)
    return valor

def diminuir(valor, porcentagem):
    porcentagem = porcentagem / 100
    valor = valor * (1 - porcentagem)
    return valor

def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2

def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


#JEITO GUANABARA
'''
from os import replace


def aumentar(valor, porcentagem):
    valor = valor + (1 * porcentagem / 100)
    return valor

def diminuir(valor, porcentagem):
    porcentagem = porcentagem / 100
    valor = valor * (1 - porcentagem)
    return valor

def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')'
'''