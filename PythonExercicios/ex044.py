print('='*30)
print('Calculando forma de pagamento')
print('='*30)
valorProduto = float(input('Digite o valor do produto: R$'))
print('='*30)
print('Formas de pagamento:\n1 - Á vista (dinheiro ou cheque)\n2 - Á vista no cartão\n3 - Até 2x no cartão\n4 - 3x ou mais no cartão')
pagamento = int(input('Selecione a forma de pagamento: '))


if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
    if pagamento == 1:
        total = valorProduto - (valorProduto * 10) / 100
        print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(valorProduto, total))
    elif pagamento == 2:
        total = valorProduto - (valorProduto * 5) / 100
        print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(valorProduto, total))
    elif pagamento == 4:
        parcela = int(input('Quantas parcelas:'))
        total = valorProduto + (valorProduto * 20) / 100
        valorParcela = total / parcela
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, valorParcela))
        print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(valorProduto, total))
    else:
        print('O valor do produto é R$ {:.2f}'.format(valorProduto))
else:
    print('Opção inválida, tente novamente!')