galera = list()
dados = list()
totalMaiorDeIdade = totalMenorDeIdade = 0
for contador in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    print(galera)
    print(dados)
    dados.clear() # clear vai limpar a lista dados. Dados vai funcionar como uma váriavel, mas sendo lista e armazenando mais informação
    print(dados)
print(galera)

#Mostrar pessoas com mais de 21 anos
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
        totalMaiorDeIdade += 1
    else:
        print(f'{pessoa[0]} é menor de idade')
        totalMenorDeIdade += 1
print(f'Temos {totalMaiorDeIdade} maiores e {totalMenorDeIdade} menores de idade.')