def ficha(name = '', gols = 0):
    if name == '':
        name = '<desconhecido>'
    return (f'O jogador {name} fez {gols} gol(s) no campeonato')




nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite a quantidade de gols na jogador: '))
if gols == '':
    gols = 0
resultado = ficha(nome, gols)
print(resultado)