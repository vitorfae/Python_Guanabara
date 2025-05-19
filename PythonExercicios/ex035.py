triangulo = []
triangulo.append(float(input('Digite a primeira reta: ')))
triangulo.append(float(input('Digite a segunda reta: ')))
triangulo.append(float(input('Digite a terceira reta: ')))
print(triangulo)
if (triangulo[0] == triangulo[1]) and (triangulo[0] == triangulo[2]):
    print('Esse pode ser um triangulo')
else:
    print('Esse não pode ser um triangulo')