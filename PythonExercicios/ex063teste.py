numeroElemento = int(input('Digite o termo que deseja saber na sequência de Fibonacci: '))
c = 0
inicial = 0
ultimo = 1
resultado = 0
proximoPasso = 0
numeroElemento = numeroElemento - 2

#print('{} -> {} ->'.format(c, ultimo), end='')

while c <= numeroElemento:
    proximoPasso = inicial + ultimo
    resultado = ultimo + proximoPasso
    ultimo = proximoPasso
    proximoPasso = resultado
    print('{} -> '.format(resultado), end='')
    c += 1