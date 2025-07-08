fatorial = int(input('Digite um numero para saber seu fatorial? '))
print('{}!='.format(fatorial), end='')
resultado = fatorial
while fatorial != 1:
    if fatorial == 1:
        print('{}'.format(fatorial))
    else:
        print('{}X'.format(fatorial), end='')
    fatorial -= 1
    resultado = resultado * fatorial
print('1=',end='')
print(resultado)