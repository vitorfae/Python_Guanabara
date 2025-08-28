pessoas = list()
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa['sexo'] == 'F' or pessoa['sexo'] == 'M':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        seguir = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if seguir == 'S' or seguir == 'N':
            break
        else:
            print('ERRO! Resposta apenas S ou N')
    if seguir == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
somaIdade = 0
mulheres = []
for pessoa in pessoas:
    for chave, valor in pessoa.items():
        if chave == 'idade':
            somaIdade += valor
        if chave == 'sexo' and valor == 'F':
            mulheres.append(pessoa['nome'])
mediaIdade = somaIdade / len(pessoas)
print(f'B) A média de idade é de {mediaIdade:5.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}')
print('D) Lista das pessoas que estão acima da média:')
for pessoa in pessoas:
    if pessoa['idade'] >= mediaIdade:
        print(f'{pessoa};')
print('<<ENCERRADO>>')

#JEITO GUANABARA
'''
# Coleta de dados
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Resposta apenas S ou N')
    if resposta == 'N':
            break
# Tratamento de dados
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ',end='')
        for chave, valor in p.items():
            print(f'{chave} = {valor}; ', end='')
        print()
print('<<ENCERRADO>>')'''