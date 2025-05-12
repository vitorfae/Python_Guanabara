print('PROGRAMA PARA CALCULAR TINTAS')
altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))
area = altura * largura
tinta = area / 2
print('Em uma parede de {}M² é necessários {} litros de tinta'.format(area, tinta))