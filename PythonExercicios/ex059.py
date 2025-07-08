from time import sleep

escolha = 0
print('-=-'*15)
print(' PROGRAMA DE EDUCACAO MATEMATICA')
print('-=-'*15)
print('Digite dois valores para a gente comecar')
print('')
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

while escolha != 5:
    print('')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NUMEROS')
    print('[5] SAIR DO PROGRAMA')
    escolha = int(input('Qual a sua escolha? '))
    if escolha < 1 or escolha > 5:
        print('ESCOLHA INVALIDA, TENTE NOVAMENTE!')
        sleep(1)
        print('-=-' * 15)
        sleep(1)
    else:
        if escolha == 1:
            soma = num1 + num2
            print('A soma entre {} + {} vale {}'.format(num1, num2, soma))
            sleep(0.2)
            print('-=-' * 15)
            sleep(1)
        elif escolha == 2:
            multiplicar = num1 * num2
            print('A multiplicacao entre {} X {} vale {}'.format(num1, num2, multiplicar))
            sleep(0.2)
            print('-=-' * 15)
            sleep(1)
        elif escolha == 3:
            maior = num1
            if num2 > maior:
                maior = num2
            print('O maior entre {} e {} vale {}'.format(num1, num2, maior))
            sleep(0.2)
            print('-=-' * 15)
            sleep(1)
        elif escolha == 4:
            num1 = int(input('Primeiro valor: '))
            num2 = int(input('Segundo valor: '))
            sleep(0.5)
            print('-=-' * 15)
            sleep(1)
        else:
            print('FIM DO PROGRAMA')


