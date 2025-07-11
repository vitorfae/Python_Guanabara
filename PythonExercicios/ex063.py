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


#JEITO GUANABARA
'''
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end=''))
contador = 3
while contador <= n:
    t3 = t1 + t2
    print('{}'.format(t3), end=''))
    t1 = t2
    t2 = t3
    contador += 1
print(' -> FIM')
'''