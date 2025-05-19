nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi {:.1f}'.format(media))
print('APROVADO!' if media >=6 else 'REPROVADO!')

#Outra maneira de fazer:
#if media >= 6:
#    print('Sua média foi boa! APROVADO!')
#else:
#    print('Sua média foi ruim! REPROVADO!')