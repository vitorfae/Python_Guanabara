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
    seguir = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while seguir not in 'SN':
        seguir = str(input('Opção inválida! Deseja continuar? [S/N] '))
        if seguir in 'N':
            break
    if seguir == 'N':
        break
print('-=' * 30)
print(jogadores)
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