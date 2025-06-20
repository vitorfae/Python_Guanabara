print('Digite suas notas para ver se está APROVADO, REPROVADO ou ficou em RECUPERAÇÃO')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
print('O aluno está ',end='')

if media < 5:
    print('REPROVADO')
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')