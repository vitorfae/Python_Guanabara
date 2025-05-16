numero = input('Digite um número de 0 a 9999: ')

print('Analisando o número {}'.format(numero))
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

# modo guanabara
#numero = int(input('informe um número'))
#unidade = numero // 1 % 10 -> ou seja ele está usando a divisão inteira por conta do // e o resto da divisão por 10.
#dezena = numero // 10 % 10
#centena = numero // 100 % 10
#milhar = numero // 1000 % 10
#print('Unidade: {}'.format(unidade))
#print('Dezena: {}'.format(dezena))
#print('centena: {}'.format(centena))
#print('Milhar: {}'.format(milhar))