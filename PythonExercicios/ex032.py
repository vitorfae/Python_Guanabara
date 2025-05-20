from datetime import date
anoBissexto = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if anoBissexto == 0:
    anoBissexto = date.today().year
if (anoBissexto % 4 == 0 and anoBissexto % 100 != 0) or (anoBissexto % 400 == 0):
    print('O ano {} é bissexto!'.format(anoBissexto))
else:
    print('O ano {} não é bissexto!'.format(anoBissexto))