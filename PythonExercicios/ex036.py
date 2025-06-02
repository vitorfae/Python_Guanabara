print('Seja bem vindo ao empréstimo para a realização da casa própria')
valorImovel = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = float(input('Quantos anos deseja pagar? '))

if anos > 0:
    anos = anos * 12
else:
    anos = anos / 12

valorParcelamento = valorImovel / anos
print(anos)
print(valorParcelamento)

if valorParcelamento <= salario * 0.3:
    print('Parabéns o seu crédito foi aprovado!')
else:
    print('Reprovado o crédito ')