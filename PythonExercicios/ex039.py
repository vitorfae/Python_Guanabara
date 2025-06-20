import datetime

print('Programa sobre alistamento militar')
alistamento = int(18)
anoAtual = int(datetime.date.today().year)
sexo = str(input('Digite seu sexo (M/F): '))
sexo = sexo.upper()
if sexo == 'M':
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = anoAtual - nascimento
    anoAlis = nascimento + alistamento
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, anoAtual))

    if idade < 18:
        print('Ainda falta {} anos para se alistar'.format(alistamento - idade))
        print('Seu alistamento será em {}.'.format(anoAlis))
    elif idade > 18:
        print('Já passou {} anos do prazo de alistamento'.format(idade - alistamento))
        print('Seu alistamento foi em {}.'.format(anoAlis))
    else:
        print('Está na hora de se alistar')
elif sexo == 'F':
    print('Mulher não precisa se alistar')
    exit()
else:
    print('Opção inválida')
    exit()