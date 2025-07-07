print('PROGRAMA PARA GERAR RANKING DE MAIOR E MENOR PESO DE 5 PESSOAS ')
maior = 0
menor = 9999
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O Maior peso foi {}KGS'.format(maior))
print('O Menor peso foi {}KGS'.format(menor))