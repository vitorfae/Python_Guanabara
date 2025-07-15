numero = soma = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma += numero
#print('A soma vale {}'.format(soma))
print(f'A soma vale {soma}')




#FUNCIONA COM A TECNICA DAS DUAS PERGUNTAS
'''
numero = soma = 0
numero = int(input('Digite um numero: '))
while numero != 999:
    soma += numero
    numero = int(input('Digite um numero: '))
print('A soma vale {}'.format(soma))
'''

#GAMBIARRA
'''
numero = soma = 0
while numero != 999:
    numero = int(input('Digite um numero: '))
    soma += numero
s -= 999
print('A soma vale {}'.format(soma))
'''
