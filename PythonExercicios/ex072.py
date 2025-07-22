tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('Tente novamente. Digite um valor entre 0 e 20: '))
    else:
        print(f'Você digitou o numero {tupla[numero]}')
        break

'''
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
numero = int(input('Digite um número entre 0 e 20: '))
while True:
    if numero < 0 or numero > 20:
        numero = int(input('Tente novamente. Digite um valor entre 0 e 20: '))
    else:
        print(f'Você digitou o numero {tupla[numero]}')
        break
'''