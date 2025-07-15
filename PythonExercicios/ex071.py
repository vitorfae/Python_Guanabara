notaDe50 = notaDe20 = notaDe10 = notaDe1 = 0
print('='*30)
print(f'{"BANCO CEV":^30}')
print('='*30)
valorDoSaque = int(input('Qual o valor do saque: R$'))
while valorDoSaque >= 50:
    valorDoSaque -= 50
    notaDe50 += 1
while valorDoSaque >= 20:
    valorDoSaque -= 20
    notaDe20 += 1
while valorDoSaque >= 10:
    valorDoSaque -= 10
    notaDe10 += 1
while valorDoSaque >= 1:
    valorDoSaque -= 1
    notaDe1 += 1
if notaDe50 > 0:
    print(f'Total de {notaDe50} cedulas de R$50,00')
if notaDe20 > 0:
    print(f'Total de {notaDe20} cedulas de R$20,00')
if notaDe10 > 0:
    print(f'Total de {notaDe10} cedulas de R$10,00')
if notaDe1 > 0:
    print(f'Total de {notaDe1} cedulas de R$1,00')
print('='*30)
print('Volte sempre ao BANCO CEV!')

'''
#JEITO GUANABARA
print('='*30)
print(f'{"BANCO CEV":^30}')
print('='*30)
valorDoSaque = int(input('Qual o valor do saque: R$'))
total = valorDoSaque
cedula = 50
totalCedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedulas += 1
    else:
        if totalCedulas > 0:
        print(f'Total de {totalCedulas} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedulas = 0
        if total == 0:
            break
'''