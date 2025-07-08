import random
from time import sleep

tentativas = 0
resposta = 0
print('-=-'*21)
print('O computador vai sortear um numero de 1 a 10, tente adivinhar!')
print('-=-'*21)
print('ESTOU PENSANDO QUAL NUMERO IREI ESCOLHER...')
for c in range(1, 22):
    print('-=-', end='')
    sleep(0.3)
print('')

numeroAleatorio = random.randint(1, 10)
while resposta != numeroAleatorio:
    resposta = int(input('Qual o numero que o computador sorteou?'))
    tentativas += 1
print('Parabens voce ACERTOU o numero sorteado ({}) com {} tentaivas'.format(numeroAleatorio, tentativas))
