n = 1
par = 0
impar = 0
print('digite varios valores e diremos quantos sao impar e quantos sao pares')
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares'.format(par, impar))