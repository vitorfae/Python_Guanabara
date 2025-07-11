# isso:
'''
num = 0
soma = 0
digitados = 0
'''

#Vira isso:
num = soma = digitados = 0

while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    soma += num
    if num == 999:
        soma -= num
        break
    else:
        digitados += 1
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(digitados, soma))


#JEITO guanabara sem precisar diminuir o 999
'''
num = soma = digitados = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    digitados += 1
    num = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(digitados, soma))
'''