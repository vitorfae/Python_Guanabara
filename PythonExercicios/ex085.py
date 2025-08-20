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

#JEITO GUANABARA
'''numeros = [[], []]
valor = 0
for contador in range(1, 8):
    valor = int(input(f'Digite o {contador}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-='*30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')'''