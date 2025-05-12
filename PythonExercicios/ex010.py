reais = float(input('Qual valor tem na sua carteira? R$'))
dolar = float(3.27)
dinheiro = reais / dolar
print('Você tem R${} reais na carteira, o dólar está no valor de U${}, o dinheiro que você tem na carteira equivale a U${:.2f} dólares'.format(reais, dolar, dinheiro))