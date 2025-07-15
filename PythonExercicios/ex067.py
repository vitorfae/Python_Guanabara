#MEU JEITO
while True:
    contador = 0
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    print('-' * 30)
    while contador <= 10:
        print(f'{numero} x {contador} = {numero * contador}')
        contador += 1
    print('-' * 30)
print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO!')

#JEITO GUANABARA
'''
while True:
    contador = 0
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    print('-' * 30)
    for contador in range(1, 11)::
        print(f'{numero} x {contador} = {numero * contador}')
    print('-' * 30)
print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO!')
'''