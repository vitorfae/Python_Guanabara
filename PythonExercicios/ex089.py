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
        notasAluno = int(input('Numero invalido! Mostrar notas de qual aluno? (999 interrompe): '))
        if notasAluno == 999:
            break
    if notasAluno == 999:
        break
    elif notasAluno <= len(dadosGerais):
        print(f'Notas de {dadosGerais[notasAluno][0]} sao [{dadosGerais[notasAluno][1][0]}, {dadosGerais[notasAluno][1][1]}]')
        print('-'*30)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

'''print(dadosGerais)
print(dadosGerais[0])
print(dadosGerais[0][0]) #tras o nome
print(dadosGerais[0][1][2]) # tras a media
#print(dadosGerais[0][2])
#print(dadosGerais[0][3])'''

#JEITO GUANABARA
'''ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-'*35)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    if opcao <= len(ficha) -1:
        print(f'Notas de {ficha[opcao][0]} sao {ficha[opcao][1]}')
print('<<< VOLTE SEMPRE >>>')'''