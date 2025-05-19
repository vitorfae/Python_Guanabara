import random
print('O computador vai sortear um número de 1 a 5, tente adivinhar!')
numerosorteado = random.randint(0, 5)
numeroescolhido = int(input('Digite o número: '))
if numeroescolhido == numerosorteado:
    print('PARABÉNS! Você acertou o numero sorteado {}!'.format(numerosorteado))
else:
    print('ERROU! Você errou, o número sorteado era {}!'.format(numerosorteado))