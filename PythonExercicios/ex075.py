valor1 = int(input('Digite um numero: '))
valor2 = int(input('Digite outro numero: '))
valor3 = int(input('Digite mais um numero: '))
valor4 = int(input('Digite o ultimo numero: '))

tupla = (valor1, valor2, valor3, valor4)

print(f'Voce digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

for pos, numero in enumerate(tupla):
    if numero == 3:
        print(f'O valor 3 apareceu na {pos}ª posicao')
if 3 not in tupla:
    print('O valor 3 nao foi digitado em nenhuma posicao')

par = () #Fica fora, senao em todas as vezes que o for for executado ele vai criar a tupla
for c in range(0, len(tupla)):
    if tupla[c] % 2 == 0:
        par = par + (tupla[c],)
print(f'Os valores pares foram: {par}')