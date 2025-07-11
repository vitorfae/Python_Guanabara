#MEU JEITO
fatorial = int(input('Digite um numero para saber seu fatorial? '))
print('Calculando {}! = '.format(fatorial), end='')
resultado = fatorial
while fatorial != 1:
    if fatorial == 1:
        print('{} '.format(fatorial))
    else:
        print('{} X '.format(fatorial), end='')
    fatorial -= 1
    resultado = resultado * fatorial
print('1 =',end=' ')
print(resultado)

'''
#JEITO GUANABARA - facil
from math import factorial
n = int(input('Digite um numero para calcular seu fatorial? '))
f = factorial(n)
print('O fatorial de {} e {}.'.format(n,f))
'''

#JEITO TRADICIONAL GUANABARA
'''
n = int(input('Digite um numero para calcular seu fatorial? '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))   
'''
