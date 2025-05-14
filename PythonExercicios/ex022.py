nome = input('Digite o seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome))
print(len(''.join(nome.split()))) #nome split vai separar cada palavra em uma array, join com o '' junta todos novamente sem espaços e o len conta a quantidade sem espaços
print(len(nome.split()[0])) #o objeto nome está sendo separado palavras em indices da arrar, o [0] fora do parenteses está invocando o primeiro indice e o len vendo quantos caracteres tem.
