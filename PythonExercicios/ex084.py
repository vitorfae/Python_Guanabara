dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida!', end=' ')
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break

for contador in range(0, len(pessoas)):
    if contador == 0:
        maior = menor = pessoas[contador][1]
    elif pessoas[contador][1] > maior:
        maior = pessoas[contador][1]
    elif pessoas[contador][1] < menor:
        menor = pessoas[contador][1]


print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'o maior peso foi de {maior:.1f}Kg. peso de ',end='')
for contador in range(0, len(pessoas)):
    if pessoas[contador][1] == maior:
        print(f'[{pessoas[contador][0]}]', end=' ')

print('')

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