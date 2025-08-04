valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for posicao, valor in enumerate(valores):
    print(f'Na posição {posicao} encontrei o valor {valor}.')
print('Cheguei ao final da lista')