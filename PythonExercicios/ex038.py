print('Digite dois números para saber qual é maior')
valor1 = int(input('Número 1: '))
valor2 = int(input('Número 2: '))

if valor1 > valor2:
    print('O primeiro número "{}" é maior que o segundo número "{}"'.format(valor1, valor2))
elif valor2 > valor1:
    print('O segundo número "{}" é maior que o primeiro número "{}"'.format(valor2, valor1))
else:
    print('Não existe valor maior, os dois são iguais "{}"'.format(valor1))