linha = list()
coluna = list()
pares = 0

for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        if valor% 2 == 0: #conferindo soma de numeros pares
            pares += valor
        coluna.append(valor)
    linha.append(coluna[:])
    coluna.clear()

print('-='*30)

for c in range(0, 3):
    for l in range(0, 3):
        print(f'[ {linha[c][l]} ]', end=' ')
    print('')

print('-='*30)

print(f'A soma dos valores pares é {pares}.')

# somando terceira coluna
somaColuna = 0
for l in range(0, 3):
    somaColuna += (linha[l][2])

print(f'A soma dos valores da terceira coluna é {somaColuna}.')

#Maior valor da linha
maiorValor = max(linha[1])
print(f'O maior valor da segunda linha é {maiorValor}.')

#JEITO GUANABARA
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = somaColuna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print('')
print('-='*30)
print(f'A soma dos valores pares é {par}')
for l in range(0, 3):
    somaColuna += (matriz[l][2])
print(f'A soma dos valores da terceira coluna é {somaColuna}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maiorValor}.')'''

