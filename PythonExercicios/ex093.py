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