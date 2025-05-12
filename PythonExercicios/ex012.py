preco = float(input('Qual o preço do produto? R$'))
preco = preco - (preco*0.05)
print('O produto na liquidação fica por R${:.2f}'.format(preco))