def fatorial(num = 1):
    f = 1
    for contador in range(num, 0, -1):
        f *= contador
    return f

'''numero = int(input('Digite um numero: '))
print(f'O fatorial de {numero} e igual a {fatorial(numero)}')'''

fatorial1 = fatorial(5)
fatorial2 = fatorial(4)
fatorial3 = fatorial()
print(f'Os resultados sao {fatorial1, fatorial2, fatorial3}')