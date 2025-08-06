valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-'*20)
print(f'Você digitou os valores {valores}')
maior = max(valores)
menor = min(valores)

indiceMaior = []
indiceMenor = []

for indice, valor in enumerate(valores):
    if valor == maior:
        indiceMaior.append(indice)

for indice, valor in enumerate(valores):
    if valor == menor:
        indiceMenor.append(indice)

print(f'O maior valor digitado foi {maior} nas posições {indiceMaior}')
print(f'O menor valor digitado foi {menor} nas posições {indiceMenor}')

#JEITO GUANABARRA
'''
listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > mai:
            maior = listanum[c]
        if listanum[c] < men:
            menor = listanum[c]
print('=-'*20)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições', end='')
for indice, valor in enumerate(listanum):
    if valor == maior:
        print(f'{indice}...', end='')}')
print()
print(f'O menor valor digitado foi {menor} nas posições', end='')
for indice, valor in enumerate(listanum):
    if valor == menor:
        print(f'{indice}...', end='')
            
'''


#Também funciona
'''valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-'*20)
print(f'Você digitou os valores {valores}')
maior = max(valores)
print(f'{valores.count(maior)}')
menor = min(valores)
print(f'{valores.count(menor)}')

posicaoMaior = [valores.index(maior)]
posicaoMenor = [valores.index(menor)]

print(f'O maior valor digitado foi {maior} nas posições {posicaoMaior}...')
print(f'O menor valor digitado foi {menor} nas posições {valores.index(menor)}...')'''