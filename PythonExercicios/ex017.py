import math

catetoOposto = float(input("Digite o cateto oposto: "))
catetoAdjacente =  float(input("Digite o cateto adjacente: "))
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa é: {:.2f}'.format(hipotenusa))