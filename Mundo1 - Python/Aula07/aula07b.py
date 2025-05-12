n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divinteira = n1 // n2
exponenciacao = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(soma, multiplicacao, divisao), end=' ')
#adicionando :.3f - quer dizer que eu quero 3 casas após o . flutuante, ou seja, float.
#deixando as duas linhas juntas, adicionando o (,end=' ') e (\n) é para quebrar linha.
print('Divisão inteira {} e potência{}'.format(divinteira, exponenciacao))