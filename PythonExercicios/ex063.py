numeroElemento = int(input('Digite o termo que deseja saber na sequência de Fibonacci: '))
c = 2
inicial = 0
ultimo = 1
resultado = 0
proximoPasso = 0
numeroElemento = numeroElemento - 2

print('{} -> {} -> {} -> '.format(inicial, ultimo, ultimo), end='')
proximoPasso = inicial + ultimo
while c <= numeroElemento:
    resultado = ultimo + proximoPasso
    ultimo = proximoPasso
    proximoPasso = resultado
    print('{} -> '.format(resultado), end='')
    c += 1
print('FIM')