import random
from time import sleep #deixa o código hibernando por um tempo desejado
print('-=-'*22)
print('O computador vai sortear um número de 1 a 5, tente adivinhar!')
print('-=-'*22)
numerosorteado = random.randint(0, 5) #faz o computador pensar
numeroescolhido = int(input('Em que número pensei? ')) #jogador digita a tentativa
print('PROCESSANDO...')
sleep(3) #Quantos segundos deseja ficar 'hibernando'.
if numeroescolhido == numerosorteado:
    print('PARABÉNS! Você acertou o numero sorteado {}!'.format(numerosorteado))
else:
    print('ERROU! Você errou, o número sorteado era {}!'.format(numerosorteado))