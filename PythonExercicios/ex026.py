frase = input('Digite uma frase: ')
quantidadeDeA = frase.lower().count('a')
print('Tem um total de {} A nessa frase!'.format(quantidadeDeA))
primeiraPosicao = frase.lower().lstrip().find('a') + 1       #frase.lower() deixa tudo minusculo -> lstrip() remove todos espaços excedentes na esquerda -> find('a') vai indicar onde está a primeira, mas como o indíce é 0 adicionamos o +1 para dizer que está na posição 1
print('A primeira posição que o A aparece é {}'.format(primeiraPosicao))
ultimaPosicao = frase.lower().lstrip().rfind('a') + 1
print('A última posição que o A aparece é {}'.format(ultimaPosicao))