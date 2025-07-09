sequencia = ''
tentativas = 0
soma = 0
mediaValores = 0
maior = 0
menor = 0

while sequencia != 'N':
    tentativas += 1
    numero = int(input('Digite um numero: '))
    sequencia = str(input('Quer continuar? [S/N] : ')).upper().strip()
    soma += numero
    mediaValores = soma / tentativas

    if tentativas == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    if sequencia == 'N':
        print('voce digitou {} numeros e a media foi {:.2f}'.format(tentativas, mediaValores))
        print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
        print('')