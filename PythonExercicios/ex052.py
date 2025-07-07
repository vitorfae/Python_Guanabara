numero = int(input('Digite um numero para saber se e primo: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\n\033[mO numero {} foi divisivel {} vezes'.format(numero, total))
if total == 2:
    print('E por isso ele e PRIMO')
else:
    print('E por isso ele nao e PRIMO')



#ERRADO
'''resultado = []
numero = int(input('Digite um numero para saber se e primo ou nao: '))
raiz = int(numero ** 0.5)
frase = ''
if numero > 1:
    for c in range(2, raiz + 1):
        valor = numero / c
        resultado.append(valor)
    for c in range(1, len(resultado) + 1):
        if type(resultado[c - 1]) == int:
            frase = 'false'
print(raiz)
print(resultado)
if frase == 'false':
    print('O numero nao e primo')
elif frase == '':
    print('O numero e primo')'''