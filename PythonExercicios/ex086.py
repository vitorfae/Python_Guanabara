linha = list()
coluna = list()

for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        coluna.append(valor)
    linha.append(coluna[:])
    coluna.clear()

print('-='*30)

for c in range(0, 3):
    for l in range(0, 3):
        print(f'[ {linha[c][l]} ]', end=' ')
    print('')

print('-='*30)

print(linha)










'''linha = list()
coluna = list()

for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        coluna.append(valor)
    linha.append(coluna[:])
    coluna.clear()

for c in range(0, 3):
    print(linha[c])'''