# PARAMETROS OPCIONAIS

'''

Passando apenas dois parametros da erro na função com 3 parametros definidos.
Mas deixando o c = 0 deixo o parametro como opcional, caso o valor não for passado ele fica com valor 0
deixando todos com 0 fica todos opcional

'''
def somar(a, b, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4) #Passando apenas dois parametros da erro na função com 3 parametros definidos

print('-' * 30)


def soma(a = 0, b = 0, c = 0):
    resultado = a + b + c
    print(f'A soma vale {resultado}')

soma()
soma(3)
soma(5, 6)
soma(8, 4, 7)