numeros = list()
pares = list()
impares = list()
for contador in range(1, 8):
    numero = int(input(f'Digite o {contador}º valor: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

numeros.append(pares)
numeros.append(impares)

print('-='*30)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')