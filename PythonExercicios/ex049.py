tabuada = int(input('Digite um número para saber a tabuada do mesmo:'))
i = 0
print('-' * 50)
for c in range(1, 11):
    resultado = tabuada * c
    print('{} x {:2} = {}'.format(tabuada, c, resultado))