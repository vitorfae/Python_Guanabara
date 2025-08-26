from random import randint

resultado = dict()
lista = list()
jogadorResultado = list()

print('Valores Sorteados:')
for contador in range(1, 5):
    resultado[f'jogador{contador}'] = int(randint(1,6))

for chave, valor in resultado.items():
    print(f'    O {chave} tirou {valor} no dado.')
    lista.append(chave)
    lista.append(valor)
    jogadorResultado.append(lista[:])
    lista.clear()
print('Ranking dos jogadores:')

for cont in range(0, len(jogadorResultado)):
    if len(lista) == 0 or lista[-1][1] <= jogadorResultado[cont][1]:
        lista.append(jogadorResultado[cont])
    else:
        i = 0
        while i <= len(lista):
            if lista[i][1] > jogadorResultado[cont][1]:
                lista.insert(i, jogadorResultado[cont])
                break
            i += 1

lista_invertida = lista[::-1]
#print(f'Lista Invertida: {lista_invertida}') - Lista invertida conferindo
i = 1
for valores in lista_invertida:
    print(f'    {i}º lugar: {valores[0]} com {valores[1]}.')
    i += 1


'''for c in range(0, len(jogadorResultado)):
    if len(lista) == 0 or lista[-1][1] <= jogadorResultado[c][1]:
        lista.append(jogadorResultado[c])
    elif jogadorResultado[c][1] <= lista[-1][1]:
        lista.insert(c -1 , jogadorResultado[c])'''


'''print(jogadorResultado)
print()
print(lista)'''

'''for indice, value in enumerate(jogadorResultado):
    print(f'{indice}, {value}')'''