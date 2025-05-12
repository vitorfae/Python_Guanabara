numero = int(input('Digite um número para descobrir o dobro, triplo e a raiz quadrada: '))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1/2) #para calcular raiz quadrada é número elevado por 1/2 e cubica 1/3.
print('O número digitado é {}, o dobro dele é {}, o triplo dele é {} e sua raiz quadrada é {:.2f}.'.format(numero, dobro, triplo, raizQuadrada))

