teste = list()

teste.append('Gustavo')
teste.append(40)
#print(teste)
galera = list()
galera.append(teste[:]) # se deixar sem a cópia ele vincula uma lista na outra
teste[0] = 'Maria'
teste [1] = 22
galera.append(teste[:]) # se deixar sem a cópia ele vincula uma lista na outra
print(galera)

# se uma vincular na outra da o seguinte resultado:
'''[['Maria', 22], ['Maria', 22]]'''
#pois o primeiro append vai subir 'Gustavo e '40', ele vai inserir e vincular na lista galera
#depois como tem o vinculo, quando alterar a lista teste ele altera a lista galera tambem pois tem vinculo e não cópia
#qunado der um append novamente ele vai adicionar novamente a lista teste com as mesma informações então duplica