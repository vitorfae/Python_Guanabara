def parOuImpar(num = 0):
    if num % 2 == 0:
        return True
    else:
        return False

numero = int(input('Digite um numero: '))
if parOuImpar(numero):
    print('E par')
else:
    print('E impar')
