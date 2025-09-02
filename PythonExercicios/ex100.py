from random import randint
from time import sleep

#Sem parametros:
def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        numero = randint(1, 10)
        numeros.append(numero)
        print(numero, end=' ')
        sleep(0.4)
    print('PRONTO!')

def somaPar():
    soma = 0
    for valores in numeros:
        if valores % 2 == 0:
            soma += valores
    print(f'Somando os valores pares de {numeros}, temos {soma}')

numeros = list()
sorteia()
somaPar()

#Com parametros:
'''def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        numero = randint(1, 10)
        lista.append(numero)
        print(numero, end=' ')
        sleep(0.4)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valores in lista:
        if valores % 2 == 0:
            soma += valores
    print(f'Somando os valores pares de {numeros}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)'''