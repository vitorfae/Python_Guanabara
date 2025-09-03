# CRIANDO MINHA PRÓPRIA DOCSTRING

'''
    Inserir aspas duplas 3X abaixo da função def

    e o texto digitado vira uma docstrings

'''

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Vitor Faé
    """
    contador = i
    while contador <= f:
        print(contador, end='..')
        contador += 1
    print('FIM!')

contador(2, 10, 2)
print('-' * 30)
help(contador)