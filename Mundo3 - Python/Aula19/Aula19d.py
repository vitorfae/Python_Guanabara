estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('sigla do estado: '))
    brasil.append(estado.copy())
print()
#Cada passada for de chave e valor ele me traz a chave e depois o valor dela respectivamente.
for estado in brasil:
    for chave, valor in estado.items(): #para chave e valor em estado.items() -> ou seja, na primeira passada ele pega o que tem na chave uf e na segunda na chave sigla e o valor delas, ou seja, uf -> valor e sigla-> valor
        print(f'O campo {chave} tem o valor {valor}')                                                                                                                                    # 'uf'-> Santa Catarina e 'sigla' -> SC
    print()
print()
print('-'*35)

# Cada passada em valor ele traz os valores do dicionario estado, que estão dentro da lista Brasil
for estado in brasil:
    for value in estado.values():
        print(value)
    print()
print()
print('-'*35)

for estado in brasil:
    for key in estado.keys():
        print(key)
    print()
print()
print('-'*35)

for estado in brasil:
    print(estado) #Traz cada indice da lista brasil, ou seja, da seguinte maneira:
# 'uf' : 'Santa Catarina', 'sigla' : 'SC'