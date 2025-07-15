total = produtosAcimaDeMil = maisBarato =  0
menorProduto = ''
print('-'*25)
print(F'{"LOJA SUPER BARATAO":^26}')
print('-'*25)
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if maisBarato == 0 or valor < maisBarato:
        maisBarato = valor
        menorProduto = nome
    if valor > 1000:
        produtosAcimaDeMil += 1
    total += valor
    if continua == 'N':
        break
print('-------- FIM DO PROGRAMA ---------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {produtosAcimaDeMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menorProduto} que custa R${maisBarato:.2f}')