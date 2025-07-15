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
print(f'Total de {notaDe50} cedulas de R$50,00')
print(f'Total de {notaDe20} cedulas de R$20,00')
print(f'Total de {notaDe10} cedulas de R$10,00')
print(f'Total de {notaDe1} cedulas de R$1,00')
print('='*30)
print('Volte sempre ao BANCO CEV!')