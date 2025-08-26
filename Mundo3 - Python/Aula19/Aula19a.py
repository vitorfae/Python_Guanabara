dados = dict() #Pode ser criado o dicionário dessa maneira
dados = {} #Acredito que dessa maneira
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
#criar e adicionar elemento
dados['sexo'] = 'Masculino'
print(dados['sexo'])
#remover elementos
del dados['idade']
print(dados)
