nome = input('Digite o seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome contando os espaços tem {} caracteres'.format(len(nome)))
print('Seu nome contando apenas as letras tem {} caracteres'.format(len(''.join(nome.split())))) #nome split vai separar cada palavra em uma array, join com o '' junta todos novamente sem espaços e o len conta a quantidade sem espaços
print('O seu primeiro nome é {} e tem {} letras'.format(len(nome.split, nome.split()[0]))) #o objeto nome está sendo separado palavras em indices da arrar, o [0] fora do parenteses está invocando o primeiro indice e o len vendo quantos caracteres tem.
