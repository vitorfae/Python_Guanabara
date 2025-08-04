'''valores = list()''' # pode iniciar a lista assim ou da maneira abaixo.
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print(valores)

for valor in valores:
    print(f'{valor} tem o valor {valor}', end='')

print('')

for indice, valor in enumerate(valores):
    print(f'Na posição {indice} encontrei o valor {valor}')
print('Cheguei ao final da lista.')
