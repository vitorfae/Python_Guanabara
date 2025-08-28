estatisticas = dict()
gols = list()
total = 0

estatisticas['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'quantas partidas {estatisticas["nome"]} jogou? '))
for part in range(0, partidas):
    gol = (int(input(f'Quantos gols na partida {part}? ')))
    total += gol
    gols.append(gol)
estatisticas['gols'] = gols[:]
estatisticas['total'] = total
print('-=' * 30)
print(estatisticas)
print('-=' * 30)
for chave, valor in estatisticas.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {estatisticas["nome"]} jogou {partidas} partidas.')
for partid in range(0, partidas):
    print(f'    => Na partida {partid}, fez {gols[partid]} gols.')
print(f'Foi um total de {estatisticas['total']} gols.')

#JEITO GUANABARA
'''jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for indice, valor in enumerate(jogador['gols']):
    print(f'    => Na partida {indice}, fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')'''