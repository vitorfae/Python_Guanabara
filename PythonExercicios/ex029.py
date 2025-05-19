velocidade = float(input('Digite a velocidade atual do veículo: '))
if velocidade > 80:
    print('Você foi multado por excesso de velocidade!')
    multa = (velocidade - 80) * 7
    print('Sua multa ficou no valor de R${:.2f}'.format(multa))
else:
    print('Você não foi multado!')