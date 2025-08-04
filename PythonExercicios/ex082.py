valores = list()
pares = list()
impares = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while fim not in 'SN':
        fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if fim in 'N':
        break

for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        pares.append(valores[c])
    else:
        impares.append(valores[c])

print('-='*20)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')