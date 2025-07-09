num = 0
soma = 0
digitados = 0

while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    soma += num
    if num == 999:
        soma -= num
        break
    else:
        digitados += 1
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(digitados, soma))



