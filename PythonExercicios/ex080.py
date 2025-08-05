valores = []

for c in range(0, 5):
    digitado = int(input('Digite um valor: '))
    while digitado in valores:
        print('Valor ja inserido, tente novamente!')
        digitado = int(input('Digite um valor: '))
    else:
        if c == 0:
            valores.append(digitado)
            print('Adicionado ao final da lista')
            #print(valores) - Ajudando a ver como o array se comporta
        else:
            for cont in range(0, len(valores)):
                if digitado < valores[cont] and digitado not in valores: # se o valor digitado for menor que valor do indice e nao estiver em valores ainda ele vai inserir antes desse valor
                    valores.insert(cont, digitado)                         #como vai gravar um por vez o menor sempre vai vir antes ou seja, por primeiro
                    print(f'Adicionado na posicao {cont} da lista')
                elif digitado > max(valores) and digitado not in valores: #senao se digitado for maior que o maior valor e nao tiver sido inserido ele vai adicionar ao final da lista
                    valores.append(digitado)
                    print('Adicionado ao final da lista')
            #print(valores) - Ajudando a ver como o array se comporta
print('-='*25)
print(f'Os valores digitados em ordem foram {valores}')