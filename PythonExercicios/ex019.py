import random
import math
from operator import index

nomes = []

while (len(nomes) < 4):
    nomes.append(input("Digite o nome: "))
escolhido = random.randint(0, (len(nomes) - 1))
print(escolhido)
print('O escolhido aleatoriamente pelo sistema foi {}!'.format(nomes[escolhido]))