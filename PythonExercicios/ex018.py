import math
grau = float(input("Digite o grau: "))
radiano = math.radians(grau)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)
print('O seno de {}ºgraus é: {:.2f}'.format(grau, seno))
print('O cosseno de {}ºgraus é: {:.2f}'.format(grau, cosseno))
print('A tangente de {}ºgraus é: {:.2f}'.format(grau, tangente))