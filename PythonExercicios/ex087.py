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