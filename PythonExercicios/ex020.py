import random
import math
from operator import index

alunos = []

while (len(alunos) < 4):
    alunos.append(input("Digite o nome do aluno: "))

random.shuffle(alunos)
print('A ordem de apresentação será \n {}'.format(alunos))