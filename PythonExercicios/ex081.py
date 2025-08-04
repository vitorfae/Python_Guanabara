valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while fim not in 'SN':
        fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if fim == 'N':
        break

valores.sort(reverse=True) # lista em ordem decrescente
print('-='*20)
print(f'Você digitou {len(valores)} valores.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')