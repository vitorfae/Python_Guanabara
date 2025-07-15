maior = homem = mulher = 0
while True:
    print('-'*25)
    print(f'{"CADASTRE UMA PESSOA":^25}')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-'*25)
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao total temos {homem} homens cadastrados')
print(f'Temos {mulher} mulheres com menos de 20 anos')