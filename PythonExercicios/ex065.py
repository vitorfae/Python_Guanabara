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

#JEITO GUANABARA
'''
resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'S':
    numero = int(input('Digite um numero: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero #nesse caso o maior e menor recebem numero caso seja o primeiro numero digitado
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] : ')).upper().strip()[0]
media = soma / quantidade
print('Voce digitou {} numeros e a media foi {}'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
'''