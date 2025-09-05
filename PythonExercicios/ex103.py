def ficha(name = '', gols = 0):
    if name == '':
        name = '<desconhecido>'
    return (f'O jogador {name} fez {gols} gol(s) no campeonato')




nome = str(input('Digite o nome do jogador: '))
gols = input('Digite a quantidade de gols na jogador: ')
if gols == '':
    gols = 0
elif gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
resultado = ficha(nome, gols)
print(resultado)

#JEITO GUANABARA

'''def ficha(jogador = '<desconhecido>', gol = 0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato')


#Programa principal
name = str(input('Digite o nome do jogador: '))
gol = str(input('Quantos gols na jogador: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if name.strip() == '':
    ficha(gols = gol)
else:
    ficha(name, gol)'''