# ESCOPO DE VÁRIAVEIS
'''

'''

def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa Principal
n = 2 # É uma váriavel global, ou seja pode ser acessada em qualquer lugar ou função.
print(f'No programa principal N vale {n}')
print('-' * 30)
teste()
print('-' * 30)
print(f'No programa principal X vale {x}') #vai dar erro, pois x é uma variavel local, pois está dentro da função