from random import randint
from time import sleep
from operator import itemgetter

resultado = dict()
lista = list()
jogadorResultado = list()

print('Valores Sorteados:')
for contador in range(1, 5):
    resultado[f'jogador{contador}'] = int(randint(1,6))

for chave, valor in resultado.items():
    print(f'    O {chave} tirou {valor} no dado.')
    sleep(0.5)
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
    sleep(0.5)
    i += 1

#JEITO GUANABARA
'''jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = dict()
print('Valores sorteados:')
for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #preciso de um novo dicionário para jogar o dicionários jogos de maneira ordenada.
                                                #key=itemgetter(1) -> se refere ao avalor da chave, ou seja, se fose 0 seria a chave: Jogador1..., como é 1 ele pega o valor da chave
#print(ranking) ranking fica como uma lista, precisamos tratar como uma lista
print('-=' * 30)
print('==RANKING JOGADORES==')
# o indice vai ser o indice da lista e o valor vai trazer o dicionário separa, ou seja o primeiro vai trazer o indice 0 da lista que tem os valores -> valor[0] = Jogador1 e valor[1] = valor do dado
#indice mais um apenas para a exibição ficar mais bonita
for indice, valor in enumerate(ranking):
    print(f'  {indice+1}º lugar: {valor[0]} com {valor[1]} no dado.')
    sleep(0.5)'''