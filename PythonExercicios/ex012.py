preco = float(input('Qual o preço do produto? R$'))
preco = preco - (preco*0.05)
print('O produto na liquidação de 5% fica por R${:.2f}'.format(preco))