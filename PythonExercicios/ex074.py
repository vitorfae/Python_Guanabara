from random import *
tuplas = ()

for c in range(0, 6):
    numeroAleatorio = int(random() * 1000)
    if c == 0 or numeroAleatorio < menor:
        menor = numeroAleatorio
    if c == 0 or numeroAleatorio > maior:
        maior = numeroAleatorio
    tuplas = tuplas + (numeroAleatorio,)


print(f'Os valores sorteados foram: {tuplas}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')

#JEITO GUANABARA
'''
from random import randint
numeros = (randint(1,10), (randint(1,10), (randint(1,10), (randint(1,10), (randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
'''
