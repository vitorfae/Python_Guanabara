triangulo = []
print('='*21)
print('ANALISANDO TRIÂNGULOS')
print('='*21)
triangulo.append(float(input('Digite a primeira reta: ')))
triangulo.append(float(input('Digite a segunda reta: ')))
triangulo.append(float(input('Digite a terceira reta: ')))
print('='*21)

if (triangulo[0] + triangulo[1]) > triangulo[2] and triangulo[1] + triangulo[2] > triangulo[0] and triangulo[2] + triangulo[0] > triangulo[1]:
    print('Pode ser um triângulo')
    if triangulo[0] == triangulo[1] and triangulo[1] == triangulo[2] and triangulo[2] == triangulo[0]:
        print('É um triângulo EQUILÁTERO')
    elif triangulo[0] == triangulo[1] or triangulo[1] == triangulo[2] or triangulo[2] == triangulo[0]:
        print('É um triângulo ISÓSCELES!')
    else:
        print('É um triângulo ESCALENO!')
else:
    print('Não pode ser um triângulo')