import random
import math
from operator import index

nomes = []

while (len(nomes) < 4):
    nomes.append(input("Digite o nome: "))
escolhido = random.randint(0, (len(nomes) - 1))
print('O escolhido aleatoriamente pelo sistema foi {}!'.format(nomes[escolhido]))


#Jeito do Guanabara
#
#n1 = str(input('Primeiro número'))
#n2 = str(input('Segundo número'))
#n3 = str(input('Terceiro número'))
#n4 = str(input('Quarto número'))
#lista = [n1, n2, n3, n4]
#escolhido = random.choice(lista)  ---> choice vai sortear um elemento da lista
#print('O aluno escolhido foi {}'.format(escolhido))