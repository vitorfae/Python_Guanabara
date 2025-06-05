import random
from time import sleep
escolhaMaquina = ['pedra', 'papel', 'tesoura']
print('-=-'*7)
print('VAMOS JOGAR JOKENPÔ')
print('-=-'*7)
sleep(0.5)
print('Escolha a sua jogada para dar sequência na disputa')
print('1 - Pedra \n2 - Papel \n3 - Tesoura')
print('-=-'*7)
sleep(0.5)
jogador = int(input('Digite sua jogada: '))

if jogador < 1 or jogador > 3 :
    if jogador < 1:
        print('Erro, O valor tem que ser maior que 0')
    elif jogador > 3:
        print('Erro, O valor tem que ser menor que 3')
else:
    vezDaMaquina = random.randint(0, 2)
    print('A máquina escolheu {}'.format(escolhaMaquina[vezDaMaquina]))

    if vezDaMaquina == jogador - 1 :
        if vezDaMaquina == 0:
            print('Deu empate! Ambos escolheram Pedra')
        elif vezDaMaquina == 1:
            print('Deu empate! Ambos escolheram Papel')
        elif vezDaMaquina == 2:
            print('Deu empate! Ambos escolheram Tesoura')

    if (vezDaMaquina == 0 and jogador == 3) or (vezDaMaquina == 1 and jogador == 1) or (vezDaMaquina == 2 and jogador == 2):
        print('A máquina ganhou')
    elif (jogador == 1 and vezDaMaquina == 2) or (jogador ==2 and vezDaMaquina == 0) or (jogador == 3 and vezDaMaquina == 1):
        print('Parabéns! Você ganhou')
