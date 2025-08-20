from random import randint
from time import sleep

print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
#print('JOGO DA MEGA SENA'.center(30)) - tambem da certo
print('-'*30)
quantidadeSorteio = int(input('Quantos jogos voce quer que eu sorteie? '))
print('-=' * 4, f'SORTEANDO {quantidadeSorteio} JOGOS', '-=' * 4)
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
    print(f'Jogo {cont + 1}: {sorted(valoresSorteio)}')
    sleep(0.5)
print(f'{"-="*5} {"< Boa Sorte! >":^10} {"-="*5}')

#JEITO GUANABARA
'''lista = list()
jogos = list()
print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-'*30)
quantidadeDeJogos = int(input('Quantos jogos voce quer que eu sorteie? '))
total = 1
while total <= quantidadeDeJogos:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f' SORTEANDO {quantidadeDeJogos} jogos', '-=' * 3)
for indice, l in enumerate(jogos): #l de lista
    print(f'Jogo {indice + 1}: {jogo}')'''