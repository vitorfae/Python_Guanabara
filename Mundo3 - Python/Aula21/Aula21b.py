# DOCSTRINGS

'''

É uma string de documentação

o help(print) é uma docstring
quando executado ele mostra a docstring do comando print
toda as funcionalidades internas tem a sua propria docstring

'''
def contador(i, f, p):
    contador = i
    while contador <= f:
        print(contador, end='..')
        contador += 1
    print('FIM!')


contador(2, 10, 2)
print('-' * 30)
help(contador)