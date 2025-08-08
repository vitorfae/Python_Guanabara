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


