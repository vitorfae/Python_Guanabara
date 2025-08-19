dadosGerais = list()
nomes = list()
notas = list()

while True:
    nomes.append(str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = float((nota1 + nota2) / 2)
    notas.append(nota1)
    notas.append(nota2)
    notas.append(media)
    nomes.append(notas[:])
    notas.clear()
    dadosGerais.append(nomes[:])
    nomes.clear()




    parar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while parar not in 'SN':
        parar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if parar in 'N':
        break
print('-'*30)
print('No. NOME     MEDIA')
print('-'*30)
for c in range(0, len(dadosGerais)):
    print(f'{c:<3} {dadosGerais[c][0]:<10} {dadosGerais[c][1][2]:.1f}')

print('-'*30)
while True:
    notasAluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notasAluno == 999:
        break
    while notasAluno > len(dadosGerais)-1:
        notasAluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if notasAluno == 999:
            break
    if notasAluno == 999:
        break
    elif notasAluno <= len(dadosGerais):
        print(f'Notas de {dadosGerais[notasAluno][0]} sao [{dadosGerais[notasAluno][1][0]}, {dadosGerais[notasAluno][1][1]}]')
        print('-'*30)


'''print(dadosGerais)
print(dadosGerais[0])
print(dadosGerais[0][0]) #tras o nome
print(dadosGerais[0][1][2]) # tras a media
#print(dadosGerais[0][2])
#print(dadosGerais[0][3])'''