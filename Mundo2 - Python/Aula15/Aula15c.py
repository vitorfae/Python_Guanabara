nome = 'Jose'
idade = 33
salario = 987.35

print(f'O {nome} tem {idade} anos') #PYTHON 3
print('O {} tem {} anos'.format(nome, idade)) #PYTHON 3
print('O %s tem %s anos' % (nome, idade)) #PYTHON 2
print('')
print(f'O {nome} tem {idade} anos e ganha R$ {salario:.2f}')