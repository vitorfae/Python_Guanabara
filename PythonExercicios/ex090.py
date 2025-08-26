aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
else:
    aluno['situacao'] = 'REPROVADO'
for chave, valor in aluno.items():
    print(f'{chave} é igual a {valor}')