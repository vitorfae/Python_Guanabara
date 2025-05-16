nome = input('Digite o seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome contando os espaços tem {} caracteres'.format(len(nome)))
print('Seu nome contando apenas as letras tem {} caracteres'.format(len(''.join(nome.split())))) #nome split vai separar cada palavra em uma array, join com o '' junta todos novamente sem espaços e o len conta a quantidade sem espaços
print('O seu primeiro nome é {} e tem {} letras'.format(nome.split()[0], len(nome.split()[0]))) #o objeto nome está sendo separado palavras em indices da arrar, o [0] fora do parenteses está invocando o primeiro indice e o len vendo quantos caracteres tem.


#jeito do guanabara de contar as letras sem espaço -> (len(nome)) - nome.count(' ')
# o primeiro aqui de cima (len(nome)) vai contar os caracteres - (menos) nome.count(' ') -> diminui o valor dos caracteres espaços

#Jeito guanabara de achar o primeiro nome -> nome.find(' '), pois vai entregar onde está o primeiro espaço, que significa o primeiro nome

#pode ser feio o último da maneira a seguir:
# criar um array -> separa = nome.split() -> vai separar por palavras
#dai para exibir o primeiro nome chama da seguinte maneira -> separa[0] e para ver o tamanho -> len(separa[0])