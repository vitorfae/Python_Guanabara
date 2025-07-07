numeros = 0
print('='*20)
print('Soma de números inteiros pares')
print('='*20)
for c in range(1, 7):
    numero = int(input('Digite o {}º valor: '.format(c)))
    if numero % 2 == 0: #se o numero for par vai somar na conta
        numeros += numero
print('A soma de todos os valores pares digitados é {}'.format(numeros))
