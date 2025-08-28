jogadores = list()
while True:
    estatisticas = dict()
    gols = list()
    total = 0
    print('-' * 60)
    estatisticas['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'quantas partidas {estatisticas["nome"]} jogou? '))
    for part in range(0, partidas):
        gol = (int(input(f'Quantos gols na partida {part}? ')))
        total += gol
        gols.append(gol)
    estatisticas['gols'] = gols[:]
    estatisticas['total'] = total
    jogadores.append(estatisticas.copy())
    estatisticas.clear()
    gols.clear()
    while True:
        seguir = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if seguir == 'S' or seguir == 'N':
            break
        else:
            print('ERRO! Resposta apenas S ou N')
    if seguir == 'N':
        break
#print('-=' * 30)
#print(jogadores)
print('-=' * 30)
print(f'{"COD":<3} {"NOME":<15} {"GOLS"} {"TOTAL":>20}')
print('-' * 60)

for jogador in jogadores:
    print(f'{jogadores.index(jogador):>3}',end='')
    print(f' {jogador['nome']:<15} {jogador["gols"]} ', end='')
    print(f'{'':<5}',end='')
    print(f' {jogador["total"]:>10}')

while True:
    print('-' * 60)
    levantamento = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if levantamento == 999:
        print('<< VOLTE SEMPRE >>')
        break
    elif levantamento > len(jogadores) or levantamento < 0:
        print(f'Erro! Não existe jogador com o código {levantamento}! Tente novamente.')
    else:
        print(f'-- Levantamento do jogador {jogadores[levantamento]['nome']}')
        i = 0
        for jogador in jogadores[levantamento]['gols']:
                print(f'No jogo {jogador} fez {jogadores[levantamento]["gols"][i]} gols')
                i += 1



'''for chave, valor in estatisticas.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {estatisticas["nome"]} jogou {partidas} partidas.')
for partid in range(0, partidas):
    print(f'    => Na partida {partid}, fez {gols[partid]} gols.')
print(f'Foi um total de {estatisticas['total']} gols.')'''


#JEITO GUANABARA
'''#Colerta de dados
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp == 'S' or resp == 'N':
            break
        else:
            print('ERRO! Resposta apenas S ou N')
    if resp == 'N':
        break
# Tratamento de dados
print('cod ', end='')
for i in jogador.keys(): #traz a chave de cada item do dicionário
    print(f'{i:<15}', end='') # ou seja, primeiro i é nome, segundo gols e terceiro total
print()
print('-' * 40)
for chave, valor in enumerate(time): # chave vai trazer o indice da lista time e valor vai trazer o valor que é o dicionário incluido na lista
    print(f'{chave:>3} ', end='') # chave traz o indice da lista
    for dado in valor.values():
        print(f' {str(dado):<15}', end='') #dado vai ser o valor de cada chave do dicionario que esta dentro da lista, ou seja apenas o nome do jogador, depois os gols e depois o resultado final
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time) or busca < 0:
        print(f'ERRO! Não existe jogador com sódigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for indice, gol in enumerate(time[busca]["gols"]):
            print(f'    => Na partida {indice + 1}, fez {gol} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')'''