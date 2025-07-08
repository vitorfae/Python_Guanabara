c = 1
inicial = int (input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razao da progressão aritmética: '))
while c < 11:
    print(inicial)
    inicial = inicial + razao
    c += 1
print('ACABOU')