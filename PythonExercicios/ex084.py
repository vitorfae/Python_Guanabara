dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida!', end=' ')
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break

#DEFININDO MAIOR E MENOR
for contador in range(0, len(pessoas)):
    if contador == 0:
        maior = menor = pessoas[contador][1]
    elif pessoas[contador][1] > maior:
        maior = pessoas[contador][1]
    elif pessoas[contador][1] < menor:
        menor = pessoas[contador][1]


print('-='*30)
#TOTAL DE PESSOAS CADASTRADAS
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

#MAIOR PESO E FOR COM IF QUE BUSCA QUAIS PESSOAS TEM O MESMO PESO DO MAIOR
print(f'o maior peso foi de {maior:.1f}Kg. peso de ',end='')
for contador in range(0, len(pessoas)):
    if pessoas[contador][1] == maior:
        print(f'[{pessoas[contador][0]}]', end=' ')

print('')
#MAIOR PESO E FOR COM IF QUE BUSCA QUAIS PESSOAS TEM O MESMO PESO DO MENOR
print(f'o menor peso foi de {menor:.1f}Kg. peso de ', end='')
for contador in range(0, len(pessoas)):
    if pessoas[contador][1] == menor:
        print(f'[{pessoas[contador][0]}]', end=' ')

'''pessoas = []
tentativas = 0
while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    pessoas.append([nome, peso])
    print(pessoas)
    break'''

#JEITO GUANABARA
'''temporario = []
principal = []
maior = menor = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. peso de ',end='')
for pessoas in principal:
    if pessoas[1] == maior:
        print(f'[{pessoas[0]}]', end=' ')
print('')
print(f'O maior peso foi de {menor:.1f}Kg. peso de ',end='')
for pessoas in principal:
    if pessoas[1] == menor:
        print(f'[{pessoas[0]}]', end=' ')
print('')'''