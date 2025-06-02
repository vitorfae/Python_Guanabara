triangulo = []
print('='*21)
print('ANALISANDO TRIÂNGULOS')
print('='*21)
triangulo.append(float(input('Digite a primeira reta: ')))
triangulo.append(float(input('Digite a segunda reta: ')))
triangulo.append(float(input('Digite a terceira reta: ')))

if (triangulo[0] + triangulo[1]) >= triangulo[2] and triangulo[1] + triangulo[2] >= triangulo[0] and triangulo[2] + triangulo[0] >= triangulo[1]:
    print('Pode ser um triângulo')
    if triangulo[0] == triangulo[1] and triangulo[1] == triangulo[2] and triangulo[2] == triangulo[0]:
        print('É um triângulo equilátero')
    elif triangulo[0] == triangulo[1] or triangulo[1] == triangulo[2] or triangulo[2] == triangulo[0]:
        print('É um triângulo isósceles')
    else:
        print('É um triângulo escaleno')
else:
    print('Não pode ser um triângulo')