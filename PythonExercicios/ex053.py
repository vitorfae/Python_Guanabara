frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::1]
print('o inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase nao e um palindromo')


#PRIMEIRO metodo
'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase nao e um palindromo')'''


#Minha resolucao
'''frase_inicial = str(input(' Digite uma frase para saber se e um palindromo: ')).strip().upper()
frase_inicial = frase_inicial.replace(' ', '')
frase = frase_inicial
frase = frase[::-1]
if frase == frase_inicial:
    print(frase)
    print('A frase e um palindromo')
elif frase != frase_inicial:
    print(frase)
    print('A frase nao e um palindromo')'''