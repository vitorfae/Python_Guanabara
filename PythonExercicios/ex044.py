print('='*30)
print('Calculando forma de pagamento')
print('='*30)
valorProduto = float(input('Digite o valor do produto: '))
print('='*30)
print('Formas de pagamento:\n1 - Á vista (dinheiro ou cheque)\n2 - Á vista no cartão\n3 - Até 2x no cartão\n4 - 3x ou mais')
pagamento = int(input('Selecione a forma de pagamento: '))


if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
    if pagamento == 1:
        total = valorProduto - (valorProduto * 10) / 100
        print('O valor do produto é R$ {:.2f}'.format(total))
    elif pagamento == 2:
        total = valorProduto - (valorProduto * 5) / 100
        print('O valor do produto é R$ {:.2f}'.format(total))
    elif pagamento == 4:
        total = valorProduto + (valorProduto * 20) / 100
        print('O valor do produto é R$ {:.2f}'.format(total))
    else:
        print('O valor do produto é R$ {:.2f}'.format(valorProduto))
else:
    print('Opção inválida, tente novamente!')