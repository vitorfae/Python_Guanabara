c = 1
final = 11
maisTermos = 1
totalDeTermos = 0
totalDeTermos = totalDeTermos + 10

inicial = int (input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razao da progressão aritmética: '))
while maisTermos != 0:
    while c < final:
        print(inicial, end=' -> ')
        inicial = inicial + razao
        c += 1
    print('FIM')
    c = final
    maisTermos = int(input('Deseja que seja exibido mais quantos termos? '))
    totalDeTermos = totalDeTermos + maisTermos
    final = final + maisTermos
print('Progressao finalizada com {} termos mostrados'.format(totalDeTermos))