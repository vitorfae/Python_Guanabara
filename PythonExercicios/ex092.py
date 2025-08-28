from datetime import date

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
pessoa['idade'] = ano_atual - anoNascimento
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['CTPS'] == 0:
    print('-=' * 30)
    print(pessoa)
    for chave, valor in pessoa.items():
        print(f'{chave} tem o valor {valor}')
else:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['contratacao'] + 35 - anoNascimento
    print('-=' * 30)
    print(pessoa)
    for chave, valor in pessoa.items():
        print(f'{chave} tem o valor {valor}')

#JEITO GUANABARA
'''pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
pessoa['idade'] = ano_atual - anoNascimento
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['contratacao'] + 35 - anoNascimento
print('-=' * 30)
for chave, valor in pessoa.items():
    print(f'{chave} tem o valor {valor}')'''