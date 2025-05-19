anoBissexto = int(input('Digite o ano que deseja saber se é bissexto: '))
if (anoBissexto % 4 == 0 and anoBissexto % 100 != 0) or (anoBissexto % 400 == 0):
    print('O ano {} é bissexto!'.format(anoBissexto))
else:
    print('O ano {} não é bissexto!'.format(anoBissexto))