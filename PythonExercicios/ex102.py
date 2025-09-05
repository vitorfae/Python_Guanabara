def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um numero
    :param numero: O número a ser calculado
    :param show: (Opcional) Mostrar ou não a conta do fatorial
    :return: O valor do fatorial de um numero
    """

    f = 1
    for contador in range(numero, 0, -1):
        f *= contador
        if show:
            print(f'{contador}', end=' ')
            if contador != 1 and show == True:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return f


print('-' * 30)
print(fatorial(5, show = True))
print(fatorial(5, show = False))
help(fatorial)