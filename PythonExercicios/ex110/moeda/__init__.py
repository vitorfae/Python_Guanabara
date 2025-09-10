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

def resumo(valor, aumento, reducao):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')