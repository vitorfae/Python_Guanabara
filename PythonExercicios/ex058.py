#MEU JEITO
import random
from time import sleep

tentativas = 0
resposta = 0
print('-=-'*21)
print('O computador vai sortear um numero de 0 a 10, tente adivinhar!')
print('-=-'*21)
print('ESTOU PENSANDO QUAL NUMERO IREI ESCOLHER...')
for c in range(1, 22):
    print('-=-', end='')
    sleep(0.3)
print('')

numeroAleatorio = random.randint(0, 10)
while resposta != numeroAleatorio:
    resposta = int(input('Qual o numero que o computador sorteou?'))
    tentativas += 1
print('Parabens voce ACERTOU o numero sorteado ({}) com {} tentaivas'.format(numeroAleatorio, tentativas))


#JEITO GUANABARA
'''
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10')
print('Sera que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou: #enquanto acertou nao for verdadeiro ou seja, enquanto acertou nao tiver o valor verdadeiro ele continua o while
    jogador = int(input('Qual e seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais... Tente mais uma vez')
        elif jogador > computador:
            print('menos... Tente mais uma vez')
print('ACERTOU com {} tentativas. PARABENS'.format(palpites))
'''