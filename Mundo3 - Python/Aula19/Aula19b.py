filme = {'titulo' : 'Star Wars',
         'ano' : 1977,
         'diretor': 'George Lucas'
         }
print(filme)
print('')
print(filme.values()) #traz os seguintes valores -> Star Wars, 1977, George Lucas
print(filme.keys()) #Traz os seguintes valores -> Titulo, ano, diretor
print(filme.items()) #Traz os seguintes valores -> Traz as chaves e os valores.
print()
for key, value in filme.items():
    print(f'O {key} é {value}')