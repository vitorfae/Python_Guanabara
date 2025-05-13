import random
import math
from operator import index

trabalhos = []

while (len(trabalhos) < 4):
    trabalhos.append(input("Digite o nome do trabalho: "))

random.shuffle(trabalhos)
print(trabalhos)