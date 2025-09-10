def aumentar(valor, porcentagem, show = False):
    """
    -> Calcula o aumento de um determinado valor
    retornando o resultado com ou sem R$
    :param valor: passagem do valor a ser tratado no input
    :param porcentagem: porcentagem inserida a ser aumentada
    :param show: se quer mostrar com o sinal de R$
    :return: resultado reajustado com ou sem R$
    """

    valor = valor * (1 + porcentagem / 100)
    if show == True:
        return moeda(valor)
    else:
        return valor

def diminuir(valor, porcentagem, show = False):
    porcentagem = porcentagem / 100
    valor = valor * (1 - porcentagem)
    if show == True:
        return moeda(valor).replace('.', ',')
    else:
        return valor

def dobro(valor, show = False):
    valor = valor * 2
    if show == True:
        return moeda(valor).replace('.', ',')
    else:
        return valor

def metade(valor, show = False):
    valor = valor / 2
    if show == True:
        return moeda(valor).replace('.', ',')
    else:
        return valor

def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def resumo(valor, aumento, reducao):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')

    # JEITO GUANABARA
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