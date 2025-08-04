a = [2, 3, 4, 7]
b = a
'''b = a[:]'''#esse jeito não faz ligação, apenas copia todos os elementos de 'a' para 'b' usando fatiamento
# Python quando 'b' recebe 'a', ele faz uma ligação entre as duas, por isso na segunda exibição os dois
#valores são alterados.
print(a)
print(b)
print('')
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')