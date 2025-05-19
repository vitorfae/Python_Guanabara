numero = int(input('Digite um número para saber se é par ou ímpar: '))
parOuImpar = numero % 2
if parOuImpar == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))