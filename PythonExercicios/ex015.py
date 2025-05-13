diasAlugados = int(input('Quantos dias alugados? '))
KMRodados = float(input('Quantos Km rodados? '))
total = (diasAlugados * 60) + (KMRodados * 0.15)
print('O total a pagar R${:.2f}'.format(total))