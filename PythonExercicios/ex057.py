sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o seu sexo? [M/F] ')).upper()
    if sexo == 'M':
        print('Sexo Masculino')
    elif sexo == 'F':
        print('Sexo Feminino')
    else:
        print('Opcao invalida, tente novamente')
