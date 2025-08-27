pessoas = list()
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Opção Inválida! Sexo: [M/F]: ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    seguir = str(input('Quer continuar? [S/N]: ')).upper()[0]
    while seguir not in 'SN':
        seguir = str(input('Opção inválida! Quer continuar? [S/N]: ')).upper()[0]
        if seguir == 'N':
            break
    if seguir == 'N':
        break
print('-=' * 30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
somaIdade = 0
mulheres = []
for pessoa in pessoas:
    for chave, valor in pessoa.items():
        if chave == 'idade':
            somaIdade += valor
        if chave == 'sexo' and valor == 'F':
            mulheres.append(pessoa['nome'])
mediaIdade = somaIdade / len(pessoas)
print(f'- A média de idade é de {mediaIdade:.2f} anos.')
print(f'- As mulheres cadastradas foram {mulheres}')
print('- Lista das pessoas que estão acima da média:')
print()
for pessoa in pessoas:
    if pessoa['idade'] > mediaIdade:
        print(f'{pessoa};')
        print()
print('<<ENCERRADO>>')