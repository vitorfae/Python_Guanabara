galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera)
#print(galera[0])
#print(galera[0][0])
for pessoa in galera:
    print(pessoa) # traz as pessoas da lista galera, se colocar indice [0] ele traz apenas os nomes, ou seja, a array que tem os dados se chama pessoa. (apelido)

print('')
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')