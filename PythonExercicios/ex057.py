#MEU JEITO
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0] # 0 vai pegar a primeira letra e o strip remover espacos
    if sexo == 'M':
        print('Sexo Masculino')
    elif sexo == 'F':
        print('Sexo Feminino')
    else:
        print('Opcao invalida, tente novamente')

#JEITO GUANABARA
'''
sexo = str(input('informe seu sexo? [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
'''