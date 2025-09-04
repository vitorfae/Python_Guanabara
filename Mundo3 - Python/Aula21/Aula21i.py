#RETORNO DE VALORES
#AQUI VAI SO PRINTAR
def soma(a = 0, b = 0, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')

soma(3, 2, 5)
soma(2, 2)
soma(6)

print()
print('-' * 30)
print()

#AQUI COM RETORNO PARA PERSONALIZAR OS RESULTADOS
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

# resposta1 vai receber 's'
resposta1 = somar(3, 2 , 5)
resposta2 = somar(1, 7)
resposta3 = somar(4)
somaTotal = resposta1 + resposta2 + resposta3
print(f'Meus calculos deram {resposta1}, {resposta2} e {resposta3}. Que ao todo resulta em {somaTotal}')