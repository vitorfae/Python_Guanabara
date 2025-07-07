mediaIdade = 0
maiorIdade = 0
nomeHomem = ''
totalMulher = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('Idade '))
    sexo = str(input('sexo [M/F]')).upper()
    mediaIdade += idade

    if c == 1 and sexo == 'M':
        maiorIdade = idade
        nomeHomem = nome
    elif c == 1 and sexo == 'F':
        if idade < 20:
            totalMulher += 1
    else:
        if idade > maiorIdade and sexo == 'M':
            maiorIdade = idade
            nomeHomem = nome
        elif sexo == 'F' and idade < 20:
            menorIdade = idade
            nomeMulher = nome
print('A media de idade do grupo e de {} anos'.format(idade/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdade, nomeHomem))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totalMulher))