numero = input('Digite um número de 0 a 9999: ')

print(len(numero))
if len(numero) == 4:
    print('milhar {}'.format(numero[0]))
    print('centena {}'.format(numero[1]))
    print('dezena {}'.format(numero[2]))
    print('unidade {}'.format(numero[3]))
elif len(numero) == 3:
    print('centena {}'.format(numero[0]))
    print('dezena {}'.format(numero[1]))
    print('unidade {}'.format(numero[2]))
elif len(numero) == 2:
    print('dezena {}'.format(numero[0]))
    print('unidade {}'.format(numero[1]))
elif len(numero) == 1:
    print('unidade {}'.format(numero[0]))