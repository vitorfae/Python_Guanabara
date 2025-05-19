distancia = float(input('Digite a distância da viagem para calcular o gasto: '))
if distancia <= 200:
    distancia *= 0.5
    print('O valor dessa viagem para essa distância é de R${:.2f}'.format(distancia))
else:
    distancia *= 0.45
    print('O valor dessa viagem para essa distância é de R${:.2f}'.format(distancia))