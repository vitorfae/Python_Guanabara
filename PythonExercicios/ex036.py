print('Seja bem vindo ao empréstimo para a realização da casa própria')
valorImovel = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = float(input('Quantos anos deseja pagar? '))
anosExib = int(anos)

if anos > 0:
    anos = anos * 12
else:
    anos = anos / 12

valorParcelamento = valorImovel / anos
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valorImovel, anosExib, valorParcelamento))

if valorParcelamento <= salario * 0.3:
    print('Parabéns o seu crédito foi aprovado!')
else:
    print('Reprovado o crédito ')


#Como guanabara fez:
'''
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos vai pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='') end funciona para deixar a linha que está em baixo, junto com a primeira
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
'''