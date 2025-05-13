import math
grau = float(input("Digite o grau: "))
radiano = math.radians(grau)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
print('O seno de {}ºgraus é: {}'.format(grau, seno))
print('O cosseno de {}ºgraus é: {}'.format(grau, cosseno))