tabuada = int(input('Digite um número para saber a tabuada do mesmo:'))
i = 0
while (i<=10):
    resultado = tabuada * i
    print('{} X {} = {}'.format(tabuada, i, resultado))
    i += 1