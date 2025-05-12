tabuada = int(input('Digite um número para saber a tabuada do mesmo:'))
i = 0
print('-' * 12)
while (i<=10):
    resultado = tabuada * i
    print('{} X {:2} = {}'.format(tabuada, i, resultado))
    i += 1
print('-' * 12)