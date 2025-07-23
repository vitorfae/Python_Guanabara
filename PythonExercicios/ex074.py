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