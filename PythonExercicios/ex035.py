triangulo = []
print('-='*20)
print('ANALISADOR DE TRIANGULOS')
print('-='*20)
triangulo.append(float(input('Digite a primeira reta: ')))
triangulo.append(float(input('Digite a segunda reta: ')))
triangulo.append(float(input('Digite a terceira reta: ')))
if (triangulo[0] + triangulo[1]) >= triangulo[2] and triangulo[1] + triangulo[2] >= triangulo[0] and triangulo[2] + triangulo[0] >= triangulo[1]:
    print('Esse pode ser um triangulo')
else:
    print('Esse não pode ser um triangulo')