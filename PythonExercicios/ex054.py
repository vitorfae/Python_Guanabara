from datetime import date

print('Programa para analisar maioridade aos 21 anos')
ano_atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano_nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano_atual - ano_nasc >= 21:
        maior += 1
    elif ano_atual - ano_nasc < 21:
        menor += 1
print('Tem {} pessoas maiores de 21 anos e {} pessoas menores de 21 anos.'.format(maior, menor))