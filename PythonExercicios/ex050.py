numeros = 0
print('='*20)
print('Soma de números inteiros pares')
print('='*20)
for c in range(1, 7):
    numero = int(input('Digite números pares para somar: '))
    if numero % 2 == 0:
        numeros += numero
print('A soma de todos os valores pares digitados é {}'.format(numeros))
