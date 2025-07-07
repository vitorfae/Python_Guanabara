import time
print('='*42)
print('Números ímpares de 1 a 500 e múltiplos de 3')
print('='*42)
cont = 0
soma = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
        print(c)
        time.sleep(0.1)
print('A soma de todos os {} valores solicitados e {}'.format(cont, soma))