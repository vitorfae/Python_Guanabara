numero = soma = 0
digitados = 0
while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    digitados += 1
    soma += numero
print(f'A soma dos {digitados} valores foi {soma}!')