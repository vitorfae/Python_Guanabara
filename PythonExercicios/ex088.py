from random import randint
from time import sleep

print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
#print('JOGO DA MEGA SENA'.center(30)) - tambem da certo
print('-'*30)
quantidadeSorteio = int(input('Quantos jogos voce quer que eu sorteie? '))

for cont in range(0, quantidadeSorteio):
    valoresSorteio = list()
    for c in range(0, 6):
        numeroSorteio = randint(1, 60)
        if len(valoresSorteio) == 0:
            valoresSorteio.append(numeroSorteio)
        else:
            if numeroSorteio not in valoresSorteio:
                valoresSorteio.append(numeroSorteio)
            else:
                numeroSorteio = randint(1, 60)
                valoresSorteio.append(numeroSorteio)
    print(f'Jogo {cont + 1}: {valoresSorteio}')
    sleep(0.5)
print(f'{"-="*5} {"< Boa Sorte! >":^10} {"-="*5}')

