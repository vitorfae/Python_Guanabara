valores = []
while True:
    digitado = int(input('Digite um valor: '))
    if digitado not in valores:
        valores.append(digitado)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar.')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN': #caso continuar for S ou N nem entra no while.
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N': #Caso continuar for igual a N ele encerra o programa
            break
print('====== FIM DO PROGRAMA ======')
print(f'Você digitou os valores {sorted(valores)}') #sorted formata em ordem crescente