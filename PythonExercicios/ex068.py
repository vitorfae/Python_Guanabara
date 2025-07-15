from random import randint
vitoria = 0
print('=-'*12)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*12)
while True:
    computador = randint(0, 10)
    numero = int(input('Diga um valor: '))
    escolha = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    while escolha not in 'PI':
        print('escolha invalida, tente novamente')
        escolha = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    soma = computador + numero
    resultado = soma % 2
    if resultado != 0:
        resultado = 'IMPAR'
    elif resultado == 0:
        resultado = 'PAR'

    print('-'*24)
    print(f'Voce jogou {numero} e o computador {computador}. Total de {soma}. DEU {resultado}')
    print('-'*24)
    if escolha == 'P' and resultado == 'PAR' or escolha == 'I' and resultado == 'IMPAR':
        print('Voce VENCEU!')
        vitoria += 1
        print('Vamos jogar novamente...')
        print('=-' * 12)
    else:
        print('Voce perdeu!')
        break
print('=-' * 12)
print(f'GAME OVER! Voce venceu {vitoria} vezes')